"""
Structlog example configuration with FastAPI.
Features:
- async bound logger
- contextvars to log request-id and other meta data
- custom format for default logging loggers and structlog loggers
"""

import asyncio
import logging
import uuid
import time
from typing import Any

import httpx
import structlog
import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from starlette.requests import Request
from starlette.responses import Response
from structlog.contextvars import bound_contextvars


custom_logger = structlog.stdlib.get_logger("custom_logger")


async def create_task(q):
    for i in range(q):
        await custom_logger.info("run ", q=q, i=i)
        # await custom_logger.debug("debug")
        # logging.getLogger(__name__).info("test logging")
        await asyncio.sleep(0.5)


def configure_logger(enable_json_logs: bool = False):
    timestamper = structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S")

    shared_processors = [
        timestamper,
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.contextvars.merge_contextvars,
        structlog.processors.CallsiteParameterAdder(
            {
                structlog.processors.CallsiteParameter.FILENAME,
                structlog.processors.CallsiteParameter.MODULE,
                structlog.processors.CallsiteParameter.FUNC_NAME,
                structlog.processors.CallsiteParameter.THREAD,
                structlog.processors.CallsiteParameter.PROCESS_NAME,
            }
        ),
        structlog.stdlib.ExtraAdder(),
    ]

    structlog.configure(
        processors=shared_processors
        + [structlog.stdlib.ProcessorFormatter.wrap_for_formatter],
        logger_factory=structlog.stdlib.LoggerFactory(),
        # call log with await syntax in thread pool executor
        wrapper_class=structlog.stdlib.AsyncBoundLogger,
        cache_logger_on_first_use=True,
    )

    logs_render = (
        structlog.processors.JSONRenderer()
        if enable_json_logs
        else structlog.dev.ConsoleRenderer(colors=True)
    )

    _configure_default_logging_by_custom(shared_processors, logs_render)


def _configure_default_logging_by_custom(shared_processors, logs_render):
    handler = logging.StreamHandler()

    # Use `ProcessorFormatter` to format all `logging` entries.
    formatter = structlog.stdlib.ProcessorFormatter(
        foreign_pre_chain=shared_processors,
        processors=[
            _extract_from_record,
            structlog.stdlib.ProcessorFormatter.remove_processors_meta,
            logs_render,
        ],
    )

    handler.setFormatter(formatter)
    root_uvicorn_logger = logging.getLogger()
    root_uvicorn_logger.addHandler(handler)
    root_uvicorn_logger.setLevel(logging.INFO)


def _extract_from_record(_, __, event_dict):
    # Extract thread and process names and add them to the event dict.
    record = event_dict["_record"]
    event_dict["thread_name"] = record.threadName
    event_dict["process_name"] = record.processName
    return event_dict


configure_logger()

logger = structlog.stdlib.get_logger()

app = FastAPI()


@app.middleware("http")
async def logging_middleware(request: Request, call_next) -> Response:
    req_id = request.headers.get("request-id")

    structlog.contextvars.clear_contextvars()
    structlog.contextvars.bind_contextvars(
        request_id=req_id,
    )

    response: Response = await call_next(request)

    return response


@app.get("/ping", response_class=PlainTextResponse)
async def ping(q: int | None = None) -> Any:
    await logger.info("So much text/ IdontWanna see this ", kek=q)
    task = asyncio.create_task(create_task(q))
    await task
    return "pong"


if __name__ == "__main__":
    uvicorn.run(app)
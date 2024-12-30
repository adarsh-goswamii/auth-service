from fastapi import Request, status
# from src.main import app
from src.exceptions.errors.generic import FileUploadException
from starlette.responses import JSONResponse
from utils.response import error_response

def register_handlers(app):
  @app.exception_handler(FileUploadException)
  async def file_upload_exception_handler(request: Request, exception: FileUploadException):
    content = error_response(exception.message)
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=content.dict())
    
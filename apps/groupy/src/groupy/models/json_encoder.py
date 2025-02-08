import json
from groupy.models.file_info import FileInfo
import dataclassy
from groupy.models.file_refactoring_plan import FileRefactoringPlan


class JSONEncoderException(Exception):
    pass


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (FileInfo, FileRefactoringPlan)):
            return dataclassy.as_dict(obj)

        try:
            return super().default(obj)
        except Exception as e:
            raise JSONEncoderException(f"Error: {e}")

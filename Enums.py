from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"

class ReportFileType(str, Enum):
    CSV = "csv"
    EXCEL = "excel"
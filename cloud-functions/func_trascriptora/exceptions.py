class AudioDownloaderError(Exception):
    def __init__(self, exception: Exception):
        super().__init__()
        self.exception_invoking_the_class = exception

    def _call_common_logic(self):
        if isinstance(self.exception_invoking_the_class, ):
            return[]
        
    def file_not_found_or_empty(self):
        return[]
    
    def generic_error(self):
        return[]


class TranscriptionError(Exception):
    
    def __init__(self, exception: Exception):
        super().__init__()
        self.exception_invoking_the_class = exception

    def _call_common_logic(self):
        if isinstance(self.exception_invoking_the_class, FileNotFoundError):
            return self.file_not_found_or_empty()
        
        if isinstance():
            return


        
    def file_not_found_or_empty(self):
        return[]
    
    def speech_recognizition_error(self):
        return[]
    
    def generic_error(self):
        return[]


    


from bink.loadlib import lib, BINK_OK
import ctypes

class Tags:  
    def __init__(self, tags, c_len):    
        self._tags = tags
        self._len = c_len

    def len(self) -> int:
        return self._len
    
    def get(self, idx) -> str:
        tag = ctypes.c_char_p()
        ret = lib.bink_choices_get_text(self._tags, idx, ctypes.byref(tag))

        if ret != BINK_OK:
            raise RuntimeError("Error getting tag, index out of bounds?")

        result = tag.value.decode('utf-8')
        lib.bink_cstring_free(tag)

        return result
    
    def __del__(self):
        lib.bink_choices_free(self._tags)

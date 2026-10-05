# Режимы. Пока это просто строки, чтобы их было легко сравнивать.
MODE_GEMINI = "gemini"
MODE_TOKENS = "tokens"
MODE_EMBEDDINGS = "embeddings"


class AnalysisRequest:
    def __init__(self, source, candidate, mode):
        self.source = source
        self.candidate = candidate
        self.mode = mode


class AnalysisResult:
    def __init__(self):
        self.score = None
        self.summary = ""
        self.matches = []


class Analyzer:
    def compare(self, request):
        # Напиши здесь сравнение двух файлов.
        # request.source и request.candidate — тексты.
        # request.mode — один из режимов выше.
        # Верни AnalysisResult.
        pass

class FacebookComplianceGuard:
    BANNED_PHRASES = [
        "young",
        "male only",
        "female only",
        "native speaker",
        "under 30",
        "over 40"
    ]

    @classmethod
    def validate(cls, text: str):
        lower = text.lower()
        for phrase in cls.BANNED_PHRASES:
            if phrase in lower:
                raise ValueError(
                    f"Compliance violation detected: '{phrase}'"
                )

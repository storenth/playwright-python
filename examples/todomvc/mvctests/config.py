import os

TEST_HOST = os.getenv(
    "TEST_HOST", "business-stage.samoletx.com"
)
STAGE_HOST = os.getenv(
    "STAGE_HOST", "business-stage.samoletx.com"
)

def get_url(env):
    host = (
        STAGE_HOST
        if env == "test"
        else TEST_HOST)

    return f"https://{host}"

"""
Moodel for subtittels.

Use TypedDict to define a dict of subtitles.

Name: Subtitels
Use will how list[Subtitels] to define a list of subtitles.
"""

from typing import TypedDict


class Subtitels(TypedDict):
    """
    Subtitels dict.

    Start is a begin time of the subtitle text in seconds.
    End is an end time of the subtitle text in seconds.
    Text is a text of the subtitle.
    """

    start: float
    end: float
    text: str


class Timestamps(TypedDict):
    """
    Timestamps is a dict of timestamps.

    PARAMS
    ------
    start: float
        Start time of the subtitle text in seconds.
    end: float
        End time of the subtitle text in seconds.
    """

    start: float
    end: float

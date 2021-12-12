"""
The MIT License (MIT)

Copyright (c) 2021-Present AbstractUmbra

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from .utils import Includes


if TYPE_CHECKING:
    from .types.artist import ArtistIncludes as ArtistIncludesType
    from .types.author import AuthorIncludes as AuthorIncludesType
    from .types.chapter import ChapterIncludes as ChapterIncludesType
    from .types.cover import CoverIncludes as CoverIncludesType
    from .types.custom_list import CustomListIncludes as CustomListIncludesType
    from .types.manga import MangaIncludes as MangaIncludesType
    from .types.scanlator_group import (
        ScanlatorGroupIncludes as ScanlatorGroupIncludesType,
    )


__all__ = (
    "ArtistIncludes",
    "AuthorIncludes",
    "ChapterIncludes",
    "CoverIncludes",
    "CustomListIncludes",
    "MangaIncludes",
    "ScanlatorGroupIncludes",
)

VALID_ARTIST_INCLUDES: list[ArtistIncludesType] = ["manga"]
VALID_AUTHOR_INCLUDES: list[AuthorIncludesType] = ["manga"]
VALID_CHAPTER_INCLUDES: list[ChapterIncludesType] = ["manga", "user", "scanlation_group"]
VALID_COVER_INCLUDES: list[CoverIncludesType] = ["manga", "user"]
VALID_CUSTOMLIST_INCLUDES: list[CustomListIncludesType] = ["manga", "user", "owner"]
VALID_MANGA_INCLUDES: list[MangaIncludesType] = ["author", "artist", "cover_art", "manga"]
VALID_SCANLATORGROUP_INCLUDES: list[ScanlatorGroupIncludesType] = ["leader", "member"]


class ArtistIncludes(Includes):
    def __init__(self, *, manga: bool = True) -> None:
        self.manga = manga
        self._valid: list[ArtistIncludesType] = VALID_ARTIST_INCLUDES

    def to_query(self) -> list[str]:
        return super().to_query(valid=self._valid)


class AuthorIncludes(Includes):
    def __init__(self, *, manga: bool = True) -> None:
        self.manga = manga
        self._valid: list[AuthorIncludesType] = VALID_AUTHOR_INCLUDES

    def to_query(self) -> list[str]:
        return super().to_query(valid=self._valid)


class ChapterIncludes(Includes):
    def __init__(self, *, manga: bool = True, user: bool = True, scanlation_group: bool = True) -> None:
        self.manga = manga
        self.user = user
        self.scanlation_group = scanlation_group
        self._valid: list[ChapterIncludesType] = VALID_CHAPTER_INCLUDES

    def to_query(self) -> list[str]:
        return super().to_query(valid=self._valid)


class CoverIncludes(Includes):
    def __init__(self, *, manga: bool = True, user: bool = True) -> None:
        self.manga = manga
        self.user = user
        self._valid: list[CoverIncludesType] = VALID_COVER_INCLUDES

    def to_query(self) -> list[str]:
        return super().to_query(valid=self._valid)


class CustomListIncludes(Includes):
    def __init__(self, *, manga: bool = True, user: bool = True, owner: bool = True) -> None:
        self.manga = manga
        self.user = user
        self.owner = owner
        self._valid: list[CustomListIncludesType] = VALID_CUSTOMLIST_INCLUDES

    def to_query(self) -> list[str]:
        return super().to_query(valid=self._valid)


class MangaIncludes(Includes):
    def __init__(self, *, author: bool = True, artist: bool = True, cover_art: bool = True, manga: bool = True) -> None:
        self.author = author
        self.artist = artist
        self.cover_art = cover_art
        self.manga = manga
        self._valid: list[MangaIncludesType] = VALID_MANGA_INCLUDES

    def to_query(self) -> list[str]:
        return super().to_query(valid=self._valid)


class ScanlatorGroupIncludes(Includes):
    def __init__(self, *, leader: bool = True, member: bool = True) -> None:
        self.leader = leader
        self.member = member
        self._valid: list[CustomListIncludesType] = VALID_CUSTOMLIST_INCLUDES

    def to_query(self) -> list[str]:
        return super().to_query(valid=self._valid)

from __future__ import annotations
import dataclasses
from ..shared import channelmetadata as shared_channelmetadata
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetRTChannelsResponse:
    channels: Optional[list[shared_channelmetadata.ChannelMetadata]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channels'), 'exclude': lambda f: f is None }})
    
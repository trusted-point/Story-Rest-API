import base64
from fastapi import Query, HTTPException
from typing import Optional
from protobuf.src.cosmospy_protobuf.cosmos.base.query.v1beta1.pagination_pb2 import PageRequest

def get_pagination_params(
    key: Optional[str] = Query(default=None, description="key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set.",
                               alias="pagination.key"),
    offset: Optional[int] = Query(default=None, description="offset is a numeric offset that can be used when key is unavailable.It is less efficient than using key. Only one of offset or key should be set.",
                                  alias="pagination.offset",
                                  ge=0),
    limit: Optional[int] = Query(default = None, description="limit is the total number of results to be returned in the result page.If left empty it will default to a value to be set by each app.",
                                 alias="pagination.limit",
                                 ge=0),
    count_total: Optional[bool] = Query(default=None, description="count_total is set to true to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set.",
                                        alias="pagination.count_total"),
    reverse: Optional[bool] = Query(default=None, description="reverse is set to true if results are to be returned in the descending order.",
                                    alias="pagination.reverse"),
) -> PageRequest:
    if key:
        try:
            key_bytes = base64.b64decode(key)
        except (TypeError, base64.binascii.Error) as e:
            raise HTTPException(status_code=400, detail=f"Invalid base64 encoding for pagination key: {e}")
    else:
        key_bytes = b''

    return PageRequest(key=key_bytes, offset=offset, limit=limit, count_total=count_total, reverse=reverse)
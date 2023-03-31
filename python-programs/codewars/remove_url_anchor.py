def remove_url_anchor(url: str) -> str:
    if "#" in url:
        url_only, _ = url.split("#")
        return url_only
    else:
        return url

def remove_pem_headers(pem_key: str) -> str:
    print(pem_key)
    # Split the string into lines and filter out the headers/footers
    lines = pem_key.strip().splitlines()
    # Remove the first and last lines (headers and footers)
    key_content = "\n".join(lines[1:-1])
    return key_content
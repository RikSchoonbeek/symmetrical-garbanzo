from pathlib import Path


# A path, or list of paths, to allow for imports.
PY_SOLCX_ALLOWED_PATHS = [
    Path("contract_manager/solidity_files/"),
    Path("contract_manager/openzeppelin-contracts/contracts/token/ERC721/extensions/"),
    Path("contract_manager/openzeppelin-contracts/contracts/access/"),
]
DOTENV_FILE_PATH = Path("/.env")

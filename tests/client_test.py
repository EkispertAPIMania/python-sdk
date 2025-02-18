from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from ekispert.client import Ekispert

class TestClient:
    def test_init(self):
        client = Ekispert('API_KEY')
        assert client.api_key == 'API_KEY'

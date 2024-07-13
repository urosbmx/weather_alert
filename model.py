from pydantic import BaseModel


class WeatherData(BaseModel):
    id: str
    lang: str
    appid: str
    units: str
    cnt: str

    @classmethod
    def generate_data(cls, id="784252", lang="sr", appid="3213", units="metric", cnt="4"):
        return cls(id=id, lang=lang, appid=appid, units=units, cnt=cnt)

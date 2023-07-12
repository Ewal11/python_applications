from pydantic import BaseModel, BaseSettings
from typing import Optional

from datetime import datetime


class HodlHodlOfferBase(BaseModel):
    trading_type_name: str
    trading_type_slug: str
    # We will query our database depending on this key
    coin_currency: str
    fiat_currency: str
    # Need to make below type optional as it may return None
    payment_method_slug: Optional[str]
    payment_method_name: Optional[str]

    country_code: str
    min_trade_size: str
    max_trade_size: str

    margin_percentage: float

    offer_identifier: str
    site_name: str

    headline: str


class HodlHodlUserBase(BaseModel):
    @classmethod
    def convert_date(cls, date):
        last_online = datetime.fromtimestamp(date).strftime("%Y-%m-%d")

        return last_online

    def __init__(self, **data):
        # data["last_seen"] = self.convert_date(data["last_seen"])
        return super().__init__(**data)

    username: str
    feedback_type: str = 'SCORE'
    feedback_score: float
    trade_volume: Optional[str]
    completed_trades: int

    profile_image: Optional[str]
    # 'seller_name': offer.get("trader").get("login"),
    # 'seller_rating': offer.get("trader").get("rating"),
    # 'seller_trades_count': offer.get("trader").get("trades_count"),
    # 'seller_url': offer.get("trader").get("url")


class Settings(BaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = "utf-8"


settings = Settings()


class LogConfiguration:
    logger_name: str = "Python Application-main"
    # The below format represents: timestamp of log, log level (INFO, ERROR, ...), name of logger, path of file where
    # error occurred, line number, function name, and the custom message we added
    logger_formatter: str = "%(asctime)s-%(levelname)s-%(name)s-%(process)d-%(pathname)s|%(lineno)s:: %(funcName)s|%(" \
                            "lineno)s:: %(message)s "
    # Name of file where logs will be created
    log_file_base_name: str = "log"

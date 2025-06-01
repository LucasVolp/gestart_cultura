from fastapi import FastAPI
from modules.event import EventRouters
from modules.user import UserRouters
from modules.tier import TierRouters
from modules.ticket import TicketRouters
from modules.receipt import ReceiptRouters
from modules.purchase import PurchaseRouters
import uvicorn

app = FastAPI(title="Gestart Cultura API", version="1.0.0")

app.include_router(EventRouters)
app.include_router(UserRouters)
app.include_router(TierRouters)
app.include_router(TicketRouters)
app.include_router(ReceiptRouters)
app.include_router(PurchaseRouters)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
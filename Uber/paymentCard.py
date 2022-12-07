from payment import Payment

class PaymentCard(Payment):
  cuenta      = int
  banco       = str
  datoTarjeta = []
  
  def __init__(self):
    super().__init__()
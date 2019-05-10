""" Users module urls """


from engine.route import Router
from users.views import get_me


router = Router()
router.get('getMe', get_me.Route)

""" Users module urls """


from engine.route import Router
from users.views import get_me, create


router = Router()
router.post('create', create.Route)
router.get('getMe', get_me.Route)

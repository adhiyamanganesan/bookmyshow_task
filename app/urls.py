from app import appbuilder
from .views import *

appbuilder.app.add_url_rule("/main", view_func=main_page)

appbuilder.app.add_url_rule("/login_page", view_func=login)

appbuilder.app.add_url_rule("/resister_view", methods=["POST"], view_func=resister_view)

appbuilder.app.add_url_rule("/login_view", methods=["POST"], view_func=login_view)

appbuilder.app.add_url_rule("/booking/<user_id>", view_func=booking)

appbuilder.app.add_url_rule("/ticket_booking/<user_id>", methods=["POST"], view_func=ticket_booking)

appbuilder.app.add_url_rule("/history/<user_id>", view_func=history)

appbuilder.app.add_url_rule("/cancelled/<user_id>", view_func=cancel_page)

appbuilder.app.add_url_rule("/cancel_ticket/<user_id>", methods=["POST"],view_func=cancel_ticket)
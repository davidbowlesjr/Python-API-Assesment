from flask_restx import reqparse


post_user_serializer = reqparse.RequestParser()
post_user_serializer.add_argument("email", required=True)
post_user_serializer.add_argument("password", required=True)
post_user_serializer.add_argument("reTypedPassword", required=True, )
post_user_serializer.add_argument("orgName", required=True)
post_user_serializer.add_argument("firstName", required=True)
post_user_serializer.add_argument("lastName", required=True)

post_register_serializer = reqparse.RequestParser()
post_register_serializer.add_argument("email", required=True)
post_register_serializer.add_argument("password", required=True)
post_register_serializer.add_argument("reTypedPassword", required=True, )
post_register_serializer.add_argument("orgName", required=True)
post_register_serializer.add_argument("firstName", required=True)
post_register_serializer.add_argument("lastName", required=True)


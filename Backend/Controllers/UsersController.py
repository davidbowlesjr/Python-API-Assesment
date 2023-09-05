from Services.UserService import UserService
from flask import Flask, render_template, jsonify, request, abort
from flask_cors import CORS, cross_origin
from flask_restx import Namespace, Resource, fields
from Serializers.serializers import post_user_serializer
from structlog import get_logger

from Services.crudUser import (
    get_user_by_email,
    create_user,
    #update_movie,
    delete_user
)

logger = get_logger(__name__)

service = UserService

users_namespace = Namespace("users", description = "Register User")

#ViewModel (OUTPUT)
user = users_namespace.model(
    "User",
    {
        "id": fields.Integer(readOnly=True),
        "email": fields.String(required=True),
        "password": fields.String(required=True),
        "orgName": fields.String(required=True),
        "firstName": fields.String(required=True),
        "lastName": fields.String(required=True)
    },
)
class CreateUser(Resource):
#Login is a post request Returns User Info JSON
    @users_namespace.expect(post_user_serializer, validate=True)
    @users_namespace.marshal_with(user)
    def post(self):
        """creates a single user"""
        logger.debug("User.POST")
        args = post_user_serializer.parse_args()
        return create_user(args["email"], args["password"], 
                    args["orgName"], args["firstName"], args["lastName"])

users_namespace.add_resource(CreateUser, "")




from Services.UserService import UserService
from flask import Flask, render_template, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_restx import Namespace, Resource, fields
from Serializers.serializers import post_register_serializer
from structlog import get_logger

from Services.crudUser import (
    get_user_by_email,
)

logger = get_logger(__name__)

service = UserService

register_namespace = Namespace("register", description = "Register a new user returns private url")

#ViewModel (OUTPUT)

class RegisterUser(Resource):
#Login is a post request Returns User Info JSON
    @register_namespace.expect(post_register_serializer, validate=True)
    def post(self):
        """creates a single user"""
        logger.debug("User.POST")
        args = post_register_serializer.parse_args()

        if args["password"]!=args["reTypedPassword"]:
            return "Passwords do not match", 400

        if get_user_by_email(args["email"]) == "email Invalid":
            #TODO:Input Email Functionality
            return redirect("http://localhost:5000/users", code=307)
        else:
            return "User Already Exist", 400

register_namespace.add_resource(RegisterUser, "")




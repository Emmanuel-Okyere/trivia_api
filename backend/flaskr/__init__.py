"""Trivia API file"""
import os
import random

from flask import Flask, abort, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import Category, Question, setup_db


# paginating of questions
def paginate_questions(request, selection):
    """Paginate results"""
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    """create and configure the app"""
    app = Flask(__name__)
    setup_db(app)

    #Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    CORS(app, resources={'/': {'origins': '*'}})


    # Use the after_request decorator to set Access-Control-Allow

    @app.after_request
    def after_request(response):
        '''
        Sets access control.
        '''
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response


    # Create an endpoint to handle GET requests for all available categories.
    @app.route('/categories')
    def get_categories():
        '''
        Handles GET requests for getting all categories.
        Create an endpoint to handle GET requests
        for all available categories.
        '''

        # get all categories and add to dict
        categories = Category.query.all()
        categories_dict = {}
        for category in categories:
            categories_dict[category.id] = category.type

        # abort 404 if no categories found
        if len(categories_dict) == 0:
            abort(404)
        # return data to view
        return jsonify({
            "status": "success",
            'categories': categories_dict
        })
    @app.route("/categories", methods = ["POST"])
    def create_categories():
        """
        Create an endpoint to POST a new question,
        which will require the question and answer text,
        category, and difficulty score.

        TEST: When you submit a question on the "Add" tab,
        the form will clear and the question will appear at the end of the last page
        of the questions list in the "List" tab.
        """
        # Handles POST requests for creating new questions and searching questions.

        # load the request body
        body = request.get_json()
        # if no search term, create new question
        # load data from body
        category = body.get('type')
        print(category)
        # ensure all fields have data
        if category is None:
            abort(422)

        try:
            # create and insert new question
            category = Category(type = category)
            print(category)
            category.insert()

            # return data to view
            return jsonify({
                'status': "success",
                'details': "Category created",
                'data': {"category":category.type},
            })

        except:
            abort(422)

    @app.route("/questions")
    def get_questions():
        """
        Create an endpoint to handle GET requests for questions,
        including pagination (every 10 questions).
        This endpoint should return a list of questions,
        number of total questions, current category, categories.

        TEST: At this point, when you start the application
        you should see questions and categories generated,
        ten questions per page and pagination at the bottom of the screen for three pages.
        Clicking on the page numbers should update the questions.
        """
        questions = Question.query.all()
        total_questions = len(questions)
        current_questions = paginate_questions(request, questions)
        categories = Category.query.all()
        categories_dict = {}
        for category in categories:
            categories_dict[category.id] = category.type
        # abort 404 if no questions
        if len(current_questions) == 0:
            abort(404)
        return jsonify({
            'status': "success",
            'questions': current_questions,
            'total_questions': total_questions,
            'categories': categories_dict
        })
    @app.route("/questions/<int:question_id>", methods=['DELETE'])
    def delete_question(question_id):
        """
        Create an endpoint to DELETE question using a question ID.

        TEST: When you click the trash icon next to a question, the question will be removed.
        This removal will persist in the database and when you refresh the page.
        """
        try:
            question = Question.query.filter_by(id= question_id).one_or_none()
            if question is None:
                abort(404)
            question.delete()
            return jsonify({
                "status":"success",
                "message":f"Deleted {question_id}"
            })
        except:
            abort(422)

    @app.route("/questions", methods = ["POST"])
    def create_questions():
        """
        Create an endpoint to POST a new question,
        which will require the question and answer text,
        category, and difficulty score.

        TEST: When you submit a question on the "Add" tab,
        the form will clear and the question will appear at the end of the last page
        of the questions list in the "List" tab.
        """
        # Handles POST requests for creating new questions and searching questions.

        # load the request body
        body = request.get_json()
        # if no search term, create new question
        # load data from body
        new_question = body.get('question')
        new_answer = body.get('answer')
        new_category = body.get('category')
        new_difficulty = body.get('difficulty')
        # ensure all fields have data
        if ((new_question is None) or (new_answer is None)
                or (new_difficulty is None) or (new_category is None)):
            abort(422)

        try:
            # create and insert new question
            question = Question(question=new_question, answer=new_answer,
                                difficulty=new_difficulty, category=new_category)
            question.insert()

            # return data to view
            return jsonify({
                'status': "success",
                'details': "Question created",
                'data': {"question": question.question,"answer":question.answer,
                "difficulty":question.difficulty, "category":question.category},
            })

        except:
            abort(422)

    @app.route("/search", methods = ["POST"])
    def search_question():
        """
        Create a POST endpoint to get questions based on a search term.
        It should return any questions for whom the search term
        is a substring of the question.

        TEST: Search by any phrase. The questions list will update to include
        only question that include that string within their question.
        Try using the word "title" to start.
        """
        try:
            search = request.get_json()
            selection = Question.query.filter(
                Question.question.ilike(f'%{search["search"]}%')).all()
            # 404 if no results found
            if len(selection) == 0:
                abort(404)
            # paginate the results
            paginated = paginate_questions(request, selection)
            # return results
            return jsonify({
                'status': "success",
                'questions': paginated,
                'total_questions': len(selection)
            })
        except:
            abort(400)

    @app.route("/category/<int:category_id>/questions", methods = ["GET"])
    def get_question_by_category(category_id):
        """
        Create a GET endpoint to get questions based on category.
        TEST: In the "List" tab / main screen, clicking on one of the
        categories in the left column will cause only questions of that
        category to be shown.
        """
        question = Question.query.filter_by(category = category_id).all()
        category = Question.query.filter_by(id = category_id).one_or_none()
        if len(question) ==0 or category is None:
            abort(404)
        paginated = paginate_questions(request, question)
        return jsonify({
            "status":"success",
            "questions": paginated,
            'total_questions': len(question),
            "category": category.id
        })
    @app.route('/quiz', methods=['POST'])
    def get_random_quiz_question():
        """
        @TODO:
        Create a POST endpoint to get questions to play the quiz.
        This endpoint should take category and previous question parameters
        and return a random questions within the given category,
        if provided, and that is not one of the previous questions.

        TEST: In the "Play" tab, after a user selects "All" or a category,
        one question at a time is displayed, the user is allowed to answer
        and shown whether they were correct or not.
        """
        # Handles POST requests for playing quiz.

        # load the request body
        body = request.get_json()

        # get the previous questions
        previous = body.get('previous_question')

        # get the category
        category = body.get('category')

        # abort 400 if category or previous questions isn't found
        if ((category is None) or (previous is None)):
            abort(400)

        # load questions all questions if "ALL" is selected
        if category['id'] == 0:
            questions = Question.query.all()
        # load questions for given category
        else:
            questions = Question.query.filter_by(category=category["id"]).all()

        # get total number of questions
        total = len(questions)

        # picks a random question
        def get_random_question():
            return questions[random.randrange(0, len(questions), 1)]

        # checks to see if question has already been used
        def check_if_used(previous_question):
            used = False
            for question in previous:
                if question == previous_question.id:
                    used = True
            return used

        # get random question
        question = get_random_question()

        # check if used, execute until unused question found
        while check_if_used(question):
            question = get_random_question()

            # if all questions have been tried, return without question
            # necessary if category has <5 questions
            if len(previous) == total:
                return jsonify({
                    'status': "success"
                })

        # return the question
        return jsonify({
            'status': "success",
            'question': question.format()
        })


    @app.errorhandler(404)
    def not_found(error):
        """
        @TODO:
        Create error handlers for all expected errors
        including 404 and 422.
        """
        return jsonify({
            "status": "failure",
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "status": "failure",
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "status": "failure",
            "error": 400,
            "message": "bad request"
        }), 400

    return app

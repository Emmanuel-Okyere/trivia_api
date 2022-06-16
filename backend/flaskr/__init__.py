import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from flask_cors import CORS, cross_origin

from models import setup_db, Question, Category

# utility for paginating questions
def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    # create and configure the app
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
            'status': "success",
            'categories': categories_dict
        })

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
        # abort 404 if no questions
        if len(current_questions) == 0:
            abort(404)
        return jsonify({
            'status': "Success",
            'questions': current_questions,
            'total_questions': total_questions,
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
        print(body)
        # if search term is present
        if body.get('searchTerm'):
            search_term = body.get('searchTerm')

            # query the database using search term
            selection = Question.query.filter(
                Question.question.ilike(f'%{search_term}%')).all()

            # 404 if no results found
            if len(selection) == 0:
                abort(404)

            # paginate the results
            paginated = paginate_questions(request, selection)

            # return results
            return jsonify({
                'success': True,
                'questions': paginated,
                'total_questions': len(Question.query.all())
            })
        # if no search term, create new question
        else:
            # load data from body
            new_question = body.get('question')
            new_answer = body.get('answer')
            new_category = body.get('category')
            new_difficulty = body.get('difficulty')
            print(new_difficulty)
            # ensure all fields have data
            if ((new_question is None) or (new_answer is None)
                    or (new_difficulty is None) or (new_category is None)):
                abort(422)

            try:
                # create and insert new question
                question = Question(question=new_question, answer=new_answer,
                                    difficulty=new_difficulty, category=new_category)
                question.insert()

                # get all questions and paginate
                selection = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(request, selection)

                # return data to view
                return jsonify({
                    'success': True,
                    'created': question.id,
                    'question_created': question.question,
                    'questions': current_questions,
                    'total_questions': len(Question.query.all())
                })

            except:
                # abort unprocessable if exception
                abort(422)


    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

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

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    return app

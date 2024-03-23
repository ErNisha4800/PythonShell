


# #Arithmetic
# from flask import Flask, render_template, request
# import sys
# import io

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('shell.html')

# @app.route('/execute', methods=['POST'])
# def execute():
#     code = request.form['code']
#     sys.stdout = io.StringIO()  # Redirect stdout to capture output
#     try:
#         if "print(" in code:  # Check if the code contains "print("
#             exec(code)
#             output = sys.stdout.getvalue().strip()
#         else:
#             result = eval(code)
#             output = str(result)
#     except Exception as e:
#         output = str(e)
#     sys.stdout = sys.__stdout__  # Restore stdout
#     return output

# if __name__ == '__main__':
#     app.run(debug=True)


# numpy and panda done
# from flask import Flask, render_template, request
# import sys
# import io
# import numpy as np
# import pandas as pd


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('shell.html')

# @app.route('/execute', methods=['POST'])
# def execute():
#     code = request.form['code']
#     sys.stdout = io.StringIO()  # Redirect stdout to capture output
#     try:
#         if "print(" in code:  # Check if the code contains "print("
#             exec(code)
#             output = sys.stdout.getvalue().strip()
#         else:
#             result = eval(code)
#             output = str(result)
#     except Exception as e:
#         output = str(e)
#     sys.stdout = sys.__stdout__  # Restore stdout
#     return output

# if __name__ == '__main__':
#     app.run(debug=True)

# # math fuction 
# from flask import Flask, render_template, request
# import sys
# import io
# import numpy as np
# import pandas as pd
# import math

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('shell.html')

# @app.route('/execute', methods=['POST'])
# def execute():
#     code = request.form['code']
#     sys.stdout = io.StringIO()  # Redirect stdout to capture output
#     try:
#         if "print(" in code:  # Check if the code contains "print("
#             exec(code)
#             output = sys.stdout.getvalue().strip()
#         else:
#             result = eval(code)
#             output = str(result)
#     except Exception as e:
#         output = str(e)
#     sys.stdout = sys.__stdout__  # Restore stdout
#     return output

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request
import sys
import io
import numpy as np
import pandas as pd
import math
# import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('shell.html')

@app.route('/execute', methods=['POST'])
def execute():
    code = request.form['code']
    sys.stdout = io.StringIO()  # Redirect stdout to capture output
    try:
        if "print(" in code:  # Check if the code contains "print("
            exec(code)
            output = sys.stdout.getvalue().strip()
        else:
            result = eval(code)
            output = str(result)
    except Exception as e:
        output = str(e)
    sys.stdout = sys.__stdout__  # Restore stdout
    return output

@app.route('/capture')
def capture():
    video = cv2.VideoCapture(0)
    frames = []
    while True:
        success, frame = video.read()
        if not success:
            break
        else:
            # Perform any desired image processing operations on the frame
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Add the processed frame to the frames list
            frames.append(gray_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    video.release()
    cv2.destroyAllWindows()

    # Convert frames list to a NumPy array
    frames = np.array(frames)

    # Process the frames array further as needed

    return 'Frames captured: ' + str(frames.shape[0])

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, render_template, request
# import sys
# import io
# import numpy as np
# import pandas as pd
# import cv2

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('shell.html')

# @app.route('/execute', methods=['POST'])
# def execute():
#     code = request.form['code']
#     sys.stdout = io.StringIO()  # Redirect stdout to capture output
#     try:
#         if "print(" in code:  # Check if the code contains "print("
#             exec(code)
#             output = sys.stdout.getvalue().strip()
#         else:
#             result = eval(code)
#             output = str(result)
#     except Exception as e:
#         output = str(e)
#     sys.stdout = sys.__stdout__  # Restore stdout
#     return output

# @app.route('/test-opencv', methods=['GET'])
# def test_opencv():
#     image_path = 'image.jpg'  # Path to your image file
#     image = cv2.imread(image_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     cv2.imshow('Grayscale Image', gray)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    
#     return 'Image displayed'

# if __name__ == '__main__':
#     app.run(debug=True)


# import cv2
# from flask import Flask, render_template, request
# import sys
# import io
# import numpy as np
# import pandas as pd

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('shell.html')

# @app.route('/execute', methods=['POST'])
# def execute():
#     code = request.form['code']
#     sys.stdout = io.StringIO()  # Redirect stdout to capture output
#     try:
#         if "print(" in code:  # Check if the code contains "print("
#             exec(code)
#             output = sys.stdout.getvalue().strip()
#         else:
#             result = eval(code)
#             output = str(result)

#         # OpenCV code example
#         img = cv2.imread('path/to/output_image.jpg')
#         gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         # Perform further OpenCV operations as needed

#         # Save the modified image
#         cv2.imwrite('path/to/output_image.jpg', gray_img)

#         # Set the output message
#         output = 'Image processed and saved successfully'

#     except Exception as e:
#         output = str(e)

#     sys.stdout = sys.__stdout__  # Restore stdout
#     return output

# if __name__ == '__main__':
#     app.run(debug=True)

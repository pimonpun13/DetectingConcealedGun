from app import app
from flask import render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
import os, subprocess

app.config["VIDEO_UPLOADS"] = "/mnt/d/test/ep2/app/static/vdo/uploads"
app.config["ALLOWED_VIDEO_EXTENSIONS"] = ["MP4","MOV","AVI"]

def allowed_video(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_VIDEO_EXTENSIONS"]:
        return True
    else:
        return False

def extractvideo(videofile):
    print("extract")
    # ffmpeg  -i video_input -r 30 image/%d.jpg



@app.route("/", methods=["GET", "POST"])
def upload_video():
    if request.method == "POST":
        if request.files:
            video = request.files["video"]
            if video.filename == "":
                flash("No file", "warning")
                return redirect(request.url)
            if allowed_video(video.filename):
                filename = secure_filename(video.filename)
                video.save(os.path.join(app.config["VIDEO_UPLOADS"], filename))
                flash("Video uploaded", "success")
                print(extractvideo(filename))
                # return redirect(url_for("result_detect",filename=filename))

            else:
                flash("That file extension is not allowed", "danger")
                return redirect(request.url)
    return render_template("public/upload_video.html")


@app.route("/about")
def about():
    return render_template("public/about.html")


# @app.route("/result_detect")
# def result_detect():
#     print ("filenametest")
#     return render_template("public/result_detect.html")


@app.route("/result_detect")
def result_detect(videoname):
    print ("you win "+ videoname)
    # return render_template("public/result_detect.html")

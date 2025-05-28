from flask import Blueprint, request, jsonify
from app.database import db
from app.models.post import Post

post_bp = Blueprint("post", __name__, url_prefix="/api/posts")

# 게시글 등록 API
@post_bp.route("/", methods=["POST"])
def create_post():
    data = request.get_json()

    # 필수 필드 검사
    required_fields = ['user_id', 'title', 'content']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} 값이 누락되었습니다."}), 400

    new_post = Post(
        user_id=data["user_id"],
        title=data["title"],
        content=data["content"],
        status=data.get("status", "public")  # 기본값: public
    )

    db.session.add(new_post)
    db.session.commit()

    return jsonify({"message": "게시글이 등록되었습니다.", "post_id": new_post.post_id})

# 전체 게시글 조회 API
@post_bp.route("/", methods=["GET"])
def get_posts():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    result = []

    for post in posts:
        result.append({
            "post_id": post.post_id,
            "title": post.title,
            "content": post.content,
            "user_id": post.user_id,
            "created_at": post.created_at,
            "updated_at": post.updated_at,
            "views": post.views,
            "status": post.status
        })

    return jsonify(result)

# 단일 게시글 조회 + 조회수 증가
@post_bp.route("/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = Post.query.get(post_id)

    if not post:
        return jsonify({"error": "게시글을 찾을 수 없습니다."}), 404

    # 조회수 증가
    post.views += 1
    db.session.commit()

    return jsonify({
        "post_id": post.post_id,
        "title": post.title,
        "content": post.content,
        "user_id": post.user_id,
        "created_at": post.created_at,
        "updated_at": post.updated_at,
        "views": post.views,
        "status": post.status
    })

# 게시글 수정 API
@post_bp.route("/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    post = Post.query.get(post_id)

    if not post:
        return jsonify({"error": "게시글을 찾을 수 없습니다."}), 404

    data = request.get_json()
    title = data.get("title")
    content = data.get("content")
    status = data.get("status")

    if title:
        post.title = title
    if content:
        post.content = content
    if status:
        post.status = status

    db.session.commit()

    return jsonify({"message": "게시글이 수정되었습니다."})

# 게시글 삭제 API
@post_bp.route("/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    post = Post.query.get(post_id)

    if not post:
        return jsonify({"error": "게시글을 찾을 수 없습니다."}), 404

    db.session.delete(post)
    db.session.commit()

    return jsonify({"message": "게시글이 삭제되었습니다."})




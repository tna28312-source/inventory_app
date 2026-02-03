from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# トップ（POST検索の例）
@app.route("/inventory/", methods=["GET", "POST"])
def inventory():
    if request.method == "POST":
        item_id = request.form.get("item_id")

        if not item_id:
            # 未入力なら検索フォームへ
            return redirect(url_for("inventory_search"))

        return redirect(url_for("inventory_detail", item_id=item_id))

    return render_template("inventory.html")


@app.route("/inventory/search/", methods=["GET", "POST"])
def inventory_search():

    print("----- リクエストが来た -----")
    print("method:", request.method)
    print("args:", request.args)
    print("form:", request.form)
    print("---------------------------")

    # GET検索
    if request.method == "GET":
        item_id = request.args.get("item_id")

        if item_id:
            return redirect(url_for("inventory_detail", item_id=item_id))

    # POST検索
    if request.method == "POST":
        item_id = request.form.get("item_id")

        if item_id:
            return redirect(url_for("inventory_detail", item_id=item_id))

    # 未入力 or 初期表示
    return render_template("inventory_form.html")

# 詳細ページ
@app.route("/inventory/<int:item_id>")
def inventory_detail(item_id):
    return render_template("inventory_detail.html", item_id=item_id)


if __name__ == "__main__":
    app.run(debug=True)

# test-branchで追加したコメント
# pushのテスト
# GitHubで編集した
# pushのテスト 2回目









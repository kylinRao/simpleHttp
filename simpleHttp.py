from flask import Flask
from flask import  g
from CONSTANT import *
app = Flask(__name__)




@app.route('/',methods=["post","get"])
def hello_world():
    # print(g.index)
    # try:
    #
    #     g.index = g.index + 1;
    #     print("add one")
    # except:
    #     g.index=int(0)
    #
    # g.index = g.index + 1;
    # print(g.index)
    # g.index = int(g.index%len(duanziid_list))
    # print(g.index)
    GLOBAL_VAR.INDEX = GLOBAL_VAR.INDEX +1;
    GLOBAL_VAR.INDEX = GLOBAL_VAR.INDEX%len(GLOBAL_VAR.duanziid_list)
    return GLOBAL_VAR.resStr.format(duanziid=GLOBAL_VAR.duanziid_list[GLOBAL_VAR.INDEX])


if __name__ == '__main__':
    app.run()

import nimpy
import json

var py = pyBuiltinsModule()

proc exportToJson(questions: PyObject): string {.exportpy.} =
  echo "Created res"
  let resultJson = newJArray()
  for q in questions:
    let choices = q.choice_set.all()
    echo "Got choices ", choices
    let qjson = newJObject()
    qjson["question_text"] = %q.question_text.to(string)
    echo "Converted q to JSON ", qjson
    let choiceText = newJArray()
    for c in choices:
      add(choiceText, %c.choice_text.to(string))
    qjson["choiceText"] = choiceText
    add(resultJson, qjson)
  toUgly(result, resultJson)
  return result




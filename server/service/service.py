def request_params_handler(request):
    document = request.get_json()['params']['document']
    return document

def Service(request, document_extractor):
    document = request_params_handler(request)
    result = document_extractor.run(document)
    translated_result = [translat_obj.text for translat_obj in translator.translate(result, dest='zh-tw')]
    return {"english_result": result, "chinese_result": translated_result}

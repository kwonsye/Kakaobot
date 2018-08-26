from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from parser import *

def keyboard(request):
	return JsonResponse({
		'type':'buttons',
		'buttons':['가정폭력','성폭력','데이트폭력','신고 및 긴급상담 번호']
})

@csrf_exempt
def message(request):
	message=((request.body).decode('utf-8'))
	receivedJsonData=json.loads(message)
	content=receivedJsonData['content']

	if content=='신고 및 긴급상담 번호':
		return JsonResponse({
			'message':{
				'text':'경찰 112\n여성긴급전화 국번없이 1366\n다누리콜센터(이주여성) 1577-1366\n한국가정법률상담소 1644-7077\n대한법률구조공단 국번없이 132\n한국성폭력상담소 02-338-5801~2\n한국여성민우회 02-335-1858\n한국여성의전화 02-2263-6465\n\n긴급 사이버상담 https://pf.kakao.com/_wVVjxl#none'
},
			 'keyboard': {
                'type': 'buttons',
                'buttons': ['가정폭력', '성폭력', '데이트폭력','신고 및 긴급상담 번호']
            }
})

	if content=='가정폭력':
		return JsonResponse({
			'message':{
				'text':'1.가정폭력피해 상담소\n2.가정폭력 관련 법 및 가해자 처벌법\n3.관련 판례\n4.가정폭력 감수성 진단\n *원하는 항목을 선택해주세요.'
},
			'keyboard':{
		'type':'buttons',
		'buttons':['가정폭력피해 상담소','가정폭력 관련 법 및 가해자 처벌법','관련 판례','가정폭력 감수성 진단','처음으로']
}
})

	if content=='가정폭력피해 상담소':
		return_str=(parser.parse_domestic()).decode('utf-8')
		return JsonResponse({
			'message':{
				'text':return_str
},                  'keyboard':{
                'type':'buttons',
                'buttons':['가정폭력피해 상담소','가정폭력 관련 법 및 가해자 처>벌법','관련 판례','가정폭력 감수성 진단','처음으로']
}

})

	if content=='처음으로':
		return JsonResponse({
			'message':{
				'text':'초기 항목입니다.'
},
			'keyboard':{
		 'type': 'buttons',
                 'buttons': ['가정폭력', '성폭력', '데이트폭력','신고 및 긴급상담 번호']

}
})

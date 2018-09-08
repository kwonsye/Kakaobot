from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import json
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE","bot.settings")
#sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from .parser import *
from .models import Message
from random import *

def keyboard(request):
	return JsonResponse({
		'type':'buttons',
		'buttons':['가정폭력','성폭력','피해자분들에게 전하고 싶은 따뜻한 한 마디','당신에게 드리는 따뜻한 한 마디','신고 및 긴급상담 번호']
})

@csrf_exempt
def message(request):
	message=((request.body).decode('utf-8'))
	receivedJsonData=json.loads(message)
	content=receivedJsonData['content']

	if content=='신고 및 긴급상담 번호':
		return JsonResponse({
			'message':{
				'text':'경찰 112\n여성긴급전화(24시간 무료 운영) 국번없이 1366\n다누리콜센터(이주여성) 1577-1366\n한국가정법률상담소 1644-7077\n대한법률구조공단 국번없이 132\n한국성폭력상담소 02-338-5801~2\n한국여성민우회 02-335-1858\n한국여성의전화 02-2263-6465\n여성대상폭력범죄(성폭력/가정폭력/데이트폭력/불법촬영/스토킹/2차피해)사이버신고 http://onetouch.police.go.kr/ \n\n긴급카카오톡 사이버상담 https://pf.kakao.com/_wVVjxl#none'
},
			 'keyboard': {
                'type': 'buttons',
                'buttons': ['가정폭력', '성폭력', '피해자분들에게 전하고 싶은 따뜻한 한 마디','당신에게 드리는 따뜻한 한 마디','신고 및 긴급상담 번호']
            }
})

	if content=='가정폭력':
		return JsonResponse({
			'message':{
				'text':'1.가정폭력피해 상담소\n2.가정폭력 관련 법 및 가해자 처벌법\n3.관련 판례\n*원하는 항목을 선택해주세요.'
},
			'keyboard':{
		'type':'buttons',
		'buttons':['가정폭력피해 상담소','가정폭력 관련 법 및 가해자 처벌법','가정폭력 관련 판례','처음으로']
}
})
	if content=='가정폭력 관련 판례':
		return JsonResponse({
			'message':{
				'text':'*가정폭력 관련 판례 및 판례요지\nhttp://glaw.scourt.go.kr/wsjo/panre/sjo050.do#1535859362457\n',
},
			'keyboard':{
		'type':'buttons',
		'buttons':['가정폭력피해 상담소','가정폭력 관련 법 및 가해자 처벌법','가정폭력 관련 판례','처음으로']
}
})
	if content=='가정폭력 관련 법 및 가해자 처벌법':
		return JsonResponse({
			'message':{
				'text':'*가정폭력범죄의 처벌 등에 관한 특례법\nhttp://glaw.scourt.go.kr/wsjo/lawod/sjo190.do?contId=2241738&q=%EA%B0%80%EC%A0%95%ED%8F%AD%EB%A0%A5&nq=&w=lawod&section=lawod_nm&subw=&subsection=&subId=1&csq=&groups=2,3&category=&outmax=1&msort=&onlycount=&sp=&d1=&d2=&d3=&d4=&d5=&pg=1&p1=&p2=&p3=&p4=02&p5=&p6=&p7=&p8=&p9=&p10=&p11=&p12=&sysCd=&tabGbnCd=&saNo=&joNo=&lawNm=&hanjaYn=N&userSrchHistNo=&poption=&srch=&range=&daewbyn=N&smpryn=N&tabId=&save=Y&bubNm=#1535855031531\n\n*가정폭력방지 및 피해자보호 등에 관한 법률\nhttp://glaw.scourt.go.kr/wsjo/lawod/sjo190.do?contId=2248632&q=%EA%B0%80%EC%A0%95%ED%8F%AD%EB%A0%A5&nq=&w=lawod&section=lawod_nm&subw=&subsection=&subId=1&csq=&groups=2,3&category=&outmax=1&msort=&onlycount=&sp=&d1=&d2=&d3=&d4=&d5=&pg=2&p1=&p2=&p3=&p4=02&p5=&p6=&p7=&p8=&p9=&p10=&p11=&p12=&sysCd=&tabGbnCd=&saNo=&joNo=&lawNm=&hanjaYn=N&userSrchHistNo=&poption=&srch=&range=&daewbyn=N&smpryn=N&tabId=&save=Y&bubNm=#1535857723854\n\n',
},
			'keyboard':{
		'type':'buttons',
		'buttons':['가정폭력피해 상담소','가정폭력 관련 법 및 가해자 처벌법','가정폭력 관련 판례','처음으로']
}
})

	if content=='가정폭력피해 상담소':
		
		return JsonResponse({
			'message':{
				'text':'상담소의 지역을 입력해주세요.\n입력가능 지역:서울/부산/대구/인천/광주/대전/울산/경기/강원/충북/충남/전북/전남/경북/경남/제주/세종\n입력형식:예시)가정폭력_서울\n'
},                  'keyboard':{
                'type':'text'
               
}

})

	if content.startswith('가정폭력_'):
		area=content[5:]
		return_str=parse_domestic(area)
		return JsonResponse({
			'message':{
				'text':return_str
},                 'keyboard':{
                'type':'buttons',
                'buttons':['가정폭력피해 상담소','가정폭력 관련 법 및 가해자 처벌법','가정폭력 관련 판례','처음으로']
}
})
	if content=='성폭력':
		return JsonResponse({
			'message':{
				'text':'1.성폭력피해 상담소\n2.성폭력 관련 법 및 가해자 처벌법\n3.관련 판례\n *원하는 항목을 선택해주세요.'
},
			'keyboard':{
		'type':'buttons',
		'buttons':['성폭력피해 상담소','성폭력 관련 법 및 가해자 처벌법','성폭력 관련 판례','처음으로']
}
})
	if content=='성폭력 관련 판례':
		return JsonResponse({
			'message':{
				'text':'*성폭력 관련 판례 및 판례요지\nhttp://glaw.scourt.go.kr/wsjo/panre/sjo050.do#1535859131277\n'
},
			'keyboard':{
		'type':'buttons',
		'buttons':['성폭력피해 상담소','성폭력 관련 법 및 가해자 처벌법','성폭력 관련 판례','처음으로']
}
})

	if content=='성폭력 관련 법 및 가해자 처벌법':
		return JsonResponse({
			'message':{
				'text':'*성폭력방지 및 피해자보호 등에 관한 법률\nhttp://glaw.scourt.go.kr/wsjo/lawod/sjo190.do?contId=2248949&q=%EC%84%B1%ED%8F%AD%EB%A0%A5&nq=&w=lawod&section=lawod_nm&subw=&subsection=&subId=1&csq=&groups=2,3&category=&outmax=1&msort=&onlycount=&sp=&d1=&d2=&d3=&d4=&d5=&pg=1&p1=&p2=&p3=&p4=02&p5=&p6=&p7=&p8=&p9=&p10=&p11=&p12=&sysCd=&tabGbnCd=&saNo=&joNo=&lawNm=&hanjaYn=N&userSrchHistNo=&poption=&srch=&range=&daewbyn=N&smpryn=N&tabId=&save=Y&bubNm=#1535858070520\n\n'
},
			'keyboard':{
		'type':'buttons',
		'buttons':['성폭력피해 상담소','성폭력 관련 법 및 가해자 처벌법','성폭력 관련 판례','처음으로']
}
})

	if content=='성폭력피해 상담소':
		
		return JsonResponse({
			'message':{
				'text':'상담소의 지역을 입력해주세요.\n입력가능 지역:서울/부산/대구/인천/광주\n입력형식:예시)성폭력_서울\n'
},                  'keyboard':{
                'type':'text'
               
}

})

	if content.startswith('성폭력_'):
		area=content[4:]
		return_str=parse_sex(area)
		return JsonResponse({
			'message':{
				'text':return_str
},                 'keyboard':{
                'type':'buttons',
                'buttons':['성폭력피해 상담소','성폭력 관련 법 및 가해자 처벌법','성폭력 관련 판례','처음으로']
}
})
	if content=='피해자분들에게 전하고 싶은 따뜻한 한 마디':
	
		return JsonResponse({
			'message':{
				'text':'피해자분들께 전하고 싶은 따뜻한 말 한 마디를 적어주세요.\n당신의 한 마디가 큰 힘이 됩니다.\n\n*입력형식:피해자분들께_[전하고싶은한마디]\n[전하고싶은 한마디] 자리에 전하고 싶은 한 마디를 적어주세요. [ ]는 안쓰셔도 됩니다.'
},			'keyboard':{
				'type':'text'
       
}

})
	if content.startswith('피해자분들께_'):
		result=send_message(content)
		if result==True:
			return JsonResponse({
				'message':{
					'text':'따뜻한 한 마디가 전달되었습니다.\n당신의 작은  관심이 누군가에게 큰 힘이 되었습니다.\n'
},			
				 'keyboard': {
                			'type': 'buttons',
                			'buttons': ['가정폭력', '성폭력', '피해자분들에게 전하고 싶은 따뜻한 한 마디','당신에게 드리는 따뜻한 한 마디','신고 및 긴급상담 번호']
            }


})

	if content=='당신에게 드리는 따뜻한 한 마디':
		result=receive_message()
		return JsonResponse({
			'message':{
				'text':result
},			
				 'keyboard': {
                			'type': 'buttons',
                			'buttons': ['가정폭력', '성폭력', '피해자분들에게 전하고 싶은 따뜻한 한 마디','당신에게 드리는 따뜻한 한 마디','신고 및 긴급상담 번호']
            }


})
	
	if content=='처음으로':
		return JsonResponse({
			'message':{
				'text':'초기 항목입니다.'
},
			'keyboard':{
		 'type': 'buttons',
                 'buttons': ['가정폭력', '성폭력', '피해자분들에게 전하고 싶은 따뜻한 한 마디','당신에게 드리는 따뜻한 한 마디','신고 및 긴급상담 번호']

}
})

def send_message(message):
	result_message=message[7:]
	Message(message=result_message).save()
	
	return True

def receive_message():
	message_count=Message.objects.count()
	random_count=randint(1,message_count+1)
	try:
		random_message=Message.objects.get(pk=random_count).message
	except Message.DoesNotExist:
		random_message="고마워"
	return str(random_message)




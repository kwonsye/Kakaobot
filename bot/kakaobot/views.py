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
from .emailtest import *

def keyboard(request):
	return JsonResponse({
		'type':'buttons',
		'buttons':['가정폭력','성폭력','여성폭력 피해자 지원정책','피해자분들에게 전하고 싶은 따뜻한 한 마디','당신에게 드리는 따뜻한 한 마디','신고 및 긴급상담 번호','개발자에게 버그신고']
})

@csrf_exempt
def message(request):
	message=((request.body).decode('utf-8'))
	received_json_data=json.loads(message)
	content=received_json_data['content']

	if content=='개발자에게 버그신고':
		result=send_email()
		if result==True:
			msg='개발자에게 이메일을 보냈습니다.'
		elif result==False:
			msg=='오류가 생겨 이메일을 보내지 못했습니다.\n잠시후 다시 시도해주세요.'
		return JsonResponse({
			'message':{
				'text':msg
},
			'keyboard':{
			'type':'buttons',
			'buttons':['가정폭력','성폭력','여성폭력 피해자 지원정책','피해자분들에게 전하고 싶은 따뜻한 한 마디','당신에게 드리는 따뜻한 한 마디','신고 및 긴급상담 번호','개발자에게 버그신고']

}
})
	
	elif content=='여성폭력 피해자 지원정책':
		return JsonResponse({
			'message':{
				'text':'1.가정폭력 피해자 지원정책\n2.성폭력 피해자 지원정책\n3.성매매 피해자 지원정책\n*원하는 항목을 선택하세요.'
},
			'keyboard':{
				'type':'buttons',
				'buttons':['가정폭력 피해자 지원정책','성폭력 피해자 지원정책','성매매 피해자 지원정책']
}
			
})
	elif content=='가정폭력 피해자 지원정책':
		data=domestic_support()
		return JsonResponse({
			'message':{
				'text':data,
				'photo':{
					'url':'https://www.women1366.kr/_sub03/img/img0301_04.jpg',
					'width':850,
					'height':1151
}
},
			'keyboard':{
				'type':'buttons',
				'buttons':['가정폭력 피해자 지원정책','성폭력 피해자 지원정책','성매매 피해자 지원정책','처음으로']
}
			
})
	elif content=='성폭력 피해자 지원정책':
		return JsonResponse({
			'message':{
				'text':'*성폭력 발생 시 가장 중요한 일은 경찰에 신고 하는 것입니다.\n신고와 동시에 피해자에 대한 보호 조치가 시작됩니다.\n\n1. 전문기관에 상담 및 신고상담\n1366, 신고 112, 성폭력피해상담소,피해자를 위한 변호사 지정 및 상담,무료법률구조,의료비 지원 등\n\n2. 경찰수사\n피해자 진술조사 증거확보,가까운 해바라기를 통한 수사지원(피해자 진술조사, 영상진술 녹화, 증거채취 등)\n\n3. 검찰조사\n피해자 및 피의자 조사 기소여부 판단,영상진술 녹화,신뢰관계인 동석\n\n4. 법원재판\n가해자 처벌 피해자 보호 조치,법정동행,신변보호 위해 비공개 심리재판 청구',
				'photo':{
					'url':'https://www.women1366.kr/_sub03/img/img0301_09.jpg',
					'width':862,
					'height':680
}
},
			'keyboard':{
				'type':'buttons',
				'buttons':['가정폭력 피해자 지원정책','성폭력 피해자 지원정책','성매매 피해자 지원정책','처음으로']
}
			
})
	elif content=='성매매 피해자 지원정책':
		data=prostitution_support()
		return JsonResponse({
			'message':{
				'text':'*해외에서 성매매피해를 경험한 경우에도 긴급전화상담서비스를 이용할 수 있습니다.\n해외성매매피해자 지원을 위해 일본, 호주 등 14개국을 대상으로 UIFN서비스를 실시합니다. UIFN은 해외에 있는 성매매피해여성들이 긴급한 도움이 필요할 경우 수신자 부담으로 이용할 수 있는 국제전화이며, 이용방법은 다음과 같습니다.\n*국제전화 이용방법\n국가접속번호 + 800 + 1366 1366\n\n'+data,
				'photo':{
					'url':'https://www.women1366.kr/_sub03/img/img0303_01.jpg',
					'width':862,
					'height':745
}
},
			'keyboard':{
				'type':'buttons',
				'buttons':['가정폭력 피해자 지원정책','성폭력 피해자 지원정책','성매매 피해자 지원정책','처음으로']
}
			
})

	elif content=='신고 및 긴급상담 번호':
		return JsonResponse({
			'message':{
				'text':'경찰 112\n여성긴급전화(24시간 무료 운영) 국번없이 1366\n다누리콜센터(이주여성) 1577-1366\n한국가정법률상담소 1644-7077\n대한법률구조공단 국번없이 132\n한국성폭력상담소 02-338-5801~2\n한국여성민우회 02-335-1858\n한국여성의전화 02-2263-6465\n여성대상폭력범죄(성폭력/가정폭력/데이트폭력/불법촬영/스토킹/2차피해)사이버신고 http://onetouch.police.go.kr/ \n\n긴급카카오톡 사이버상담 https://pf.kakao.com/_wVVjxl#none'
},
			 'keyboard': {
                'type': 'buttons',
                'buttons': ['가정폭력', '성폭력','여성폭력 피해자 지원정책', '피해자분들에게 전하고 싶은 따뜻한 한 마디','당신에게 드리는 따뜻한 한 마디','신고 및 긴급상담 번호','개발자에게 버그신고']
            }
})

	elif content=='가정폭력':
		return JsonResponse({
			'message':{
				'text':'1.가정폭력피해 상담소\n2.가정폭력 관련 법 및 가해자 처벌법\n3.관련 판례\n*원하는 항목을 선택해주세요.',
				'photo':{
					'url':'https://www.women1366.kr/_sub03/img/img0301_02.jpg',
					'width':890,
					'height':690
}
},
			'keyboard':{
		'type':'buttons',
		'buttons':['가정폭력피해 상담소','가정폭력 관련 법 및 가해자 처벌법','가정폭력 관련 판례','처음으로']
}
})
	elif content=='가정폭력 관련 판례':
		data=panre_crawler('가정폭력')
		return JsonResponse({
			'message':{
				'text':data,
},
			'keyboard':{
		'type':'buttons',
		'buttons':['가정폭력피해 상담소','가정폭력 관련 법 및 가해자 처벌법','가정폭력 관련 판례','처음으로']
}
})
	elif content=='가정폭력 관련 법 및 가해자 처벌법':
		return JsonResponse({
			'message':{
				'text':'*가정폭력범죄의 처벌 등에 관한 특례법\nhttp://glaw.scourt.go.kr/wsjo/lawod/sjo190.do?contId=2241738&q=가정폭력\n\n*가정폭력방지 및 피해자보호 등에 관한 법률\nhttp://glaw.scourt.go.kr/wsjo/lawod/sjo190.do?contId=2248632&q=가정폭력\n\n',
},
			'keyboard':{
		'type':'buttons',
		'buttons':['가정폭력피해 상담소','가정폭력 관련 법 및 가해자 처벌법','가정폭력 관련 판례','처음으로']
}
})

	elif content=='가정폭력피해 상담소':
		
		return JsonResponse({
			'message':{
				'text':'상담소의 지역을 입력해주세요.\n입력가능 지역:서울/부산/대구/인천/광주/대전/울산/경기/강원/충북/충남/전북/전남/경북/경남/제주/세종\n입력형식:예시)가정폭력_서울\n'
},                  'keyboard':{
                'type':'text'
               
}

})

	elif content.startswith('가정폭력_'):
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
	elif content=='성폭력':
		return JsonResponse({
			'message':{
				'text':'1.성폭력피해 상담소\n2.성폭력 관련 법 및 가해자 처벌법\n3.관련 판례\n *원하는 항목을 선택해주세요.',
				'photo':{
					'url':'https://www.women1366.kr/_sub03/img/img0301_05.jpg',
					'width':862,
					'height':256
}
},
			'keyboard':{
		'type':'buttons',
		'buttons':['성폭력피해 상담소','성폭력 관련 법 및 가해자 처벌법','성폭력 관련 판례','처음으로']
}
})
	elif content=='성폭력 관련 판례':
		data=panre_crawler('성폭력')
		return JsonResponse({
			'message':{
				'text':data
},
			'keyboard':{
		'type':'buttons',
		'buttons':['성폭력피해 상담소','성폭력 관련 법 및 가해자 처벌법','성폭력 관련 판례','처음으로']
}
})

	elif content=='성폭력 관련 법 및 가해자 처벌법':
		return JsonResponse({
			'message':{
				'text':'*성폭력방지 및 피해자보호 등에 관한 법률\nhttp://glaw.scourt.go.kr/wsjo/lawod/sjo190.do?contId=2248949&q=성폭력\n\n'
},
			'keyboard':{
		'type':'buttons',
		'buttons':['성폭력피해 상담소','성폭력 관련 법 및 가해자 처벌법','성폭력 관련 판례','처음으로']
}
})

	elif content=='성폭력피해 상담소':
		
		return JsonResponse({
			'message':{
				'text':'상담소의 지역을 입력해주세요.\n입력가능 지역:서울/부산/대구/인천/광주\n입력형식:예시)성폭력_서울\n'
},                  'keyboard':{
                'type':'text'
               
}

})

	elif content.startswith('성폭력_'):
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
	elif content=='피해자분들에게 전하고 싶은 따뜻한 한 마디':
	
		return JsonResponse({
			'message':{
				'text':'피해자분들께 전하고 싶은 따뜻한 말 한 마디를 적어주세요.\n당신의 한 마디가 큰 힘이 됩니다.\n\n*입력형식:피해자분들께_[전하고싶은한마디]\n[전하고싶은 한마디] 자리에 전하고 싶은 한 마디를 적어주세요. [ ]는 안쓰셔도 됩니다.'
},			'keyboard':{
				'type':'text'
       
}

})
	elif content.startswith('피해자분들께_'):
		result=send_message(content)
		if result==True:
			return JsonResponse({
				'message':{
					'text':'따뜻한 한 마디가 전달되었습니다.\n당신의 작은  관심이 누군가에게 큰 힘이 되었습니다.\n'
},			
				 'keyboard': {
                			'type': 'buttons',
                			'buttons': ['가정폭력', '성폭력','여성폭력 피해자 지원정책', '피해자분들에게 전하고 싶은 따뜻한 한 마디','당신에게 드리는 따뜻한 한 마디','신고 및 긴급상담 번호','개발자에게 버그신고']
            }


})

	elif content=='당신에게 드리는 따뜻한 한 마디':
		result=receive_message()
		return JsonResponse({
			'message':{
				'text':result
},			
				 'keyboard': {
                			'type': 'buttons',
                			'buttons': ['가정폭력', '성폭력','여성폭력 피해자 지원정책', '피해자분들에게 전하고 싶은 따뜻한 한 마디','당신에게 드리는 따뜻한 한 마디','신고 및 긴급상담 번호','개발자에게 버그신고']
            }


})
	
	elif content=='처음으로':
		return JsonResponse({
			'message':{
				'text':'초기 항목입니다.'
},
			'keyboard':{
		 'type': 'buttons',
                 'buttons': ['가정폭력', '성폭력','여성폭력 피해자 지원정책', '피해자분들에게 전하고 싶은 따뜻한 한 마디','당신에게 드리는 따뜻한 한 마디','신고 및 긴급상담 번호','개발자에게 버그신고']

}
})

	else:
		return JsonResponse({
			'message':{
				'text':'입력형식에 맞게 입력해주세요!'
				},
			'keyboard':{
				'type': 'buttons',
				'buttons': ['가정폭력', '성폭력','여성폭력 피해자 지원정책', '피해자분들에게 전하고 싶은 따뜻한 한 마디','당신에게 드리는 따뜻한 한 마디','신고 및 긴급상담 번호','개발자에게 버그신고']

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




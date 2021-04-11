from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"저먼 셰퍼드,래브라도 리트리버,시베리안 허스키,포메라니안,불도그,푸들,시바견,치와와,도베르만 핀셔,로트바일러,비글,아메리칸 핏불 테리어,시추,닥스훈트,퍼그,카네코르소,말티즈,그레이트 데인,차우차우,사모예드견,버니즈 마운틴 도그,페르시아 마스티프,프렌치 불도그,요그셔 테리어,비숑 프리제,카발리에 킹찰스 스패니얼,일글리쉬 마스티프,뉴펀들랜드,복서,세인트버나드,펨브록 웰시코기,러셀 테리어,토이 푸들,보더콜리,미니어처 핀셔,잉글리시 코커 스패니얼,그레이하운드,래브라두들,보스턴 테리어,불 테리어,샤페이,바센지,캉갈 도그,하바나 실크독,말티푸,아키타견,와이머라너,달마시안,알래스칸 맬러뮤트,미니어처 슈나우저,아프간 하운드","limit":100,"print_urls":True,"format":"jpg"}
paths = response.download(arguments)
print(paths)

# 말티스,푸들,재패니스 스피츠 (Japaness Spits),치와와 (Chihuahua),Pomeranian 포메라니안,토이푸들,시츄,비숑 프리제 (Bichon Frise),닥스훈트,아메리칸 코카 스파니엘
# 요크셔테리어,래브라도 리트리버 (Labrador Retriever),비글,보더콜리,미니어쳐 핀셔 (Miniature Pinscher),골든 리트리버,진돗개,꼬똥드툴레아,시베리안 허스키 (Siberian Husky),Boston Terrier 보스턴테리어
# 알래스카 말라뮤트 (Alaskan Malamute),카디건 웰시코기,빠삐용 (Papillion),아메리칸코카스파니엘,펨브록 웰시 코기 [Pembroke Welsh Corgi],삽살개,라이카,풍산개,슈나우저,도베르만 (Dobermann)
# 샤페이 (Shar-pei),버니즈 마운틴 독 (Bernese Mountain Dog),프렌치불독,Samoyed사모예드,올드 잉글리쉬 쉽독,페키니즈 (Pekingese),퍼그 (Pug),시바견,케인코르소,브리타니 스파니엘 (Brittany Spaniel)
# 웨스트하이랜드화이트테리어,댕견,핏불테리어,포메라니안,잉글리쉬 코커 스파니엘 (English Cocker Spaniel),저먼 셰퍼드 독 (German Shepher Dog),불독,폭스테리어,롯드와일러,바셋 하운드 (Basset Houng)
# 미니어쳐슈나우저,프랜치 불독,세인트 버나드,휘핏(Whippet),불 테리어 (Bull Terrier),재패니즈 친 (재패니즈 칭),그레이트 피레니즈(Great Pyrenees),라사압소,잭 러셀 테리어(Jack Russell Terrier)
# 셔틀랜드쉽독,로트와일러 [Rottweiler],콜리,차우 차우 (Chow Chow),제주개,베들링턴 테리어,아이리쉬 울프하운드,아키타 (Akita),Collie러프 콜리,달마시안
# 바센지 (Basenji),Australian Shepherd 오스트랄리안 세퍼드,킹 찰스 스파니엘 (King Charles Spaniel),웰시코기(Welchi Corgi ),보르조이,실키테리어,카우카시안 오브차카,포인터 (Pointer),불테리어(Bull Terrier),그레이트 덴 (Great Dane)
# 벨지안 말리노이즈,불 마스티프 (Bull Mastiff),와이어 폭스 테리어,비즐라,Saint Bernard 세인트 버나드,오스트레일리안 캐틀 독 (Australian Cattle Dog),German Shepherd 저먼 세퍼드,Irish Setter 아이리시 세터,맨체스터 테리어,로디지아 리지백 (Rhodesian Ridgeback)
# 살루키 (Saluki),아프간 하운드(Afghan hounds),복서 (Boxer),제페니스친,차이니즈 크레스티드 독 (Chinese Crested Dog),Australian Cattle dog 오스트리안 캐틀독,스키퍼키 (Schipperke),아메리칸 폭스 하운드 (American Foxhound),볼조이,보스턴 테리어
# 벨지언 그로넨달,노리치 테리어 (Norwich Terrier),뉴펀들랜드 (Newfoundland),체서피크 베이 리트리버,마스티프 (Mastiff),그레이하운드 (Greyhound),Azawkh 아자와크,피니쉬 스피츠,고든 세터 (Gordon Setter),바이마라너 Weimaraner
# 티베탄 테리어 (Tibetan Terrier ),케리 블루 테리어 (Kerry Blue Terrier),엘크하운드,비어디드 콜리 (Bearded Collie),도고 알젠티노,블랙 앤 탄 쿤하운드 (Black & Tan Coonhound),혹카이도,케언테리어,에어데일 테리어 (Airedale Terrier),보더 테리어
# 아이리시 울프하운드,유라시안,Ainu 아이누,실리햄 테리어 (Sealyham Terrier),Border Collie 보더 콜리,Beagle harrier 비글해리어,딩고,스코티쉬 테리어 (Scottish Terrier),풀리 (Puli),Black Russan Terrier 블랙러시안테리어
# 방뎅,브뤼셀 그리펀 (Brussels Griffon),오스트랄리안 캘피,소프트 코티드 휘튼 테리어,Airdale Terrier 에어덜 테리어,BloodHound 블러드하운드,Cairn Terrier 케언 테리어,Scottish Terrier 스코티시 테리어,하바네제,케이스혼드 (Keeshond)
# Border Terrier 보더 테리어,Akbash dog 아카바시,세터 (Setter),잉글리쉬 쿤 하운드,블러드 하운드 (Blood hound),에스키모견,스코티쉬 디어하운드 (Scottish Deerhound),Irish Terrier 아이리시 테리어,티베탄 스파니엘 (Tibetan Spaniel),단디 디몬트
# 브리어드 (Briard),아이리쉬 테리어 (Irish Terrier),스태퍼드쉬어 불 테리어 (Staffordshire Bull Terrier,아펜핀셔 (Affenpinscher),댄디 딘몬트 테리어 (Dandie Dinmont Terrier),Basset Hound 바셑하운드,볼롱니즈,도규 대 보규옥스,플랑드르 부비에,갈고 에스파놀
# 캐넌 독,혹카이도 (Hokkaido),오스트랄리안 테리어 (Australian Terrier),Bedlington Terrier 베드링톤 테리어,오스트리안 캘피,보비에 드 플란더스 (Bouvier Des Flandres),도이치 브라케,Australian Terrier 오스트리안 테리어,Bullmastiff 불마스티프,러시안 베어 슈나우져,Appenzeller 아펜젤러
# 브라코 이탈리아노,브리쉘그리폰,블랙 앤 탄쿤 하운드,Borzoi 보르조이,치엔 크랑카이즈,드레버,베르가마스코,Belgian Griffon 벨지언 그리폰,코몬돌 (Komondor),폭스하운드, 핀란드 하운드, 던커, Billy 빌리


# 위에는 너무많아서 50개 정도로 줄임
# 저먼 셰퍼드,래브라도 리트리버,시베리안 허스키,포메라니안,불도그,푸들,시바견,치와와,도베르만 핀셔,로트바일러,비글,아메리칸 핏불 테리어,시추,닥스훈트,퍼그,카네코르소,말티즈,그레이트 데인,차우차우,사모예드견, 버니즈 마운틴 도그,페르시아 마스티프,프렌치 불도그,요그셔 테리어,비숑 프리제,카발리에 킹찰스 스패니얼,일글리쉬 마스티프,뉴펀들랜드,복서,세인트버나드,펨브록 웰시코기,러셀 테리어,토이 푸들,보더콜리,미니어처 핀셔,잉글리시 코커 스패니얼,그레이하운드,래브라두들,보스턴 테리어,불 테리어,샤페이,바센지,캉갈 도그,하바나 실크독,말티푸,아키타견,와이머라너,달마시안,알래스칸 맬러뮤트,미니어처 슈나우저,아프간 하운드

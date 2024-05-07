import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("LLAMA_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
headers = {"Authorization": f'Bearer {api_key}'}

CLASSIFICATION_LABELS = ['job title', 'company name', 'location', 'job-type', 'technologies', 'salary', 'requirements']

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def get_response(job_description):
    labels_prompt = f'You are a robot that only outputs JSON. you reply in JSON format with the fields {", ".join(CLASSIFICATION_LABELS)}'
    # details_prompt = "Example answer: {'jobTitle':'Senior Java Developer', 'companyName':'ABC'}"

    final_prompt = f'{labels_prompt} for job description: {job_description}. Respond only as shown, with no additional discursive or explanatory text.'

    output = query({
        "inputs": f'<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n{final_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n',
        "parameters": {
            "return_full_text": False,
            "max_new_tokens": 300,
            "stop": ["<|end_of_text|>", "<|eot_id|>"]
        }
    })

    return output[0]['generated_text']

if __name__ == "__main__":
    job_description1 = "Power Media Senior Java Developer Co będziesz robić Klient: Międzynarodowy software house, zajmujący się realizacją projektów na potrzeby własne oraz swoich klientów. Jest liderem w zakresie doradztwa, transformacji cyfrowej oraz dostarczania nowoczesnych rozwiązań technologicznych oraz realizuje wiele różnorodnych projektów m.in dla światowych liderów z branży motoryzacyjnej, handlowej, dystrybucyjnej, telekomunikacyjnej i publicznej. Lokalizacja biura: Gdańsk (dzielnica Przymorze, okolice stacji kolejowej Gdańsk Oliwia). Hybrydowy model pracy: 70% zdalnie, 30% z biura. Główne technologie wykorzystywane w projektach: Java, Spring Boot, Spring, Hibernate, AWS, SQL, Oracle. Firma realizuje wiele różnorodnych projektów i na etapie rozmów dopasowuje pod kątem predyspozycji, doświadczenia, zainteresowań i zapotrzebowania projektowego. Zespoły projektowe są międzynarodowe, składają się z Developerów, Analityków, Testerów, Scrum Masterów, Project Managerów. Współpracują głównie z klientami z Niemiec, Holandii, Szwajcarii, USA. Kilka wybranych projektów: 1) Logistyka/transport: automatyzacja obsługi transportu morskiego i powietrznego, projekt długoterminowy, 70% development, 30% utrzymanie, ok. 30 osób w zespole z Polski. 2) Logistyka/transport: organizacja transportu morskiego oraz lotniczego, bardzo duży projekt, długoterminowy, 50% utrzymanie, 50% development. 3) Automotive: 100% development, ok. 50 osobowy zespół (Polska, Niemcy, Indie, Portugalia). Stack technologiczny: Java, Quarkus, PostgreSQL, Angular, Kubernetes. 4) Public: aplikacja, system umożliwiający składanie wniosków online, projekt długoterminowy, 80% development, 20% utrzymanie. Jako Senior Java Developer będziesz budować i rozwijać systemy mające bezpośredni wpływ na architekturę i rozwiązania technologiczne wykorzystywane w oprogramowaniach dla światowych liderów z branży motoryzacyjnej, handlowej, dystrybucyjnej, telekomunikacyjnej i publicznej. Będziesz miał okazje rozwijać się w obszarze One Click Deployment, Clean Code, Behavior Driven Development, Automation First itp. Zakres obowiązków: tworzenie nowoczesnych aplikacji opartych o technologie Java, tworzenie rozwiązań w oparciu o wzorce projektowe i architektoniczne wykorzystując podejścia: DevOps, Domain-Driven Design, Behavior-Driven Development, TDD oraz „Infrastructure as a Service/Code”, praca z wykorzystaniem z naszych z najlepszych praktyk i metodyk zwinnych (np. Scrum, SAFe, Kanban), rozwój w obszarze profesjonalnego wytwarzania oprogramowania, Clean Code itp., ścisła współpraca z doświadczonymi ekspertami, co umożliwia szerokie możliwości pogłębiania wiedzy technicznej, biznesowej oraz umiejętności interpersonalnych. Czego oczekujemy Główne wymagania: min. 6 lat doświadczenia związanego z programowaniem w języku Java praktyczne doświadczenie z: JEE, Spring Boot, Hibernate, znajomość zasad SOLID przy tworzeniu kodu (zasada CLEAN CODE) znajomość testów jednostkowych znajomość technologii: Java 8+, Maven, Unix, Linux, Github, Bitbucket doświadczenie w projektowaniu interfejsów REST API i wdrażaniu usług RESTful doświadczenie w projektowaniu baz danych z wykorzystaniem SQL, Oracle/SQL Server, Redis; bardzo dobra znajomość języka angielskiego (min. B2). Mile widziane: znajomość technologii frontendowych: JavaScript, TypeScript, Angular, React, Vue. Jak pracujemy Code review Baza wiedzy Testy jednostkowe Automatyzacja testów Laptop Komputer stacjonarny Dodatkowy monitor Słuchawki Osobista szafka Metodyka: Scrum Możliwość zmiany projektu Benefity Pakiety i dofinansowania Pakiet medyczny Kursy językowe Szkolenia Pakiet medyczny dla rodziny Pakiet sportowy Pakiet sportowy dla rodziny Konferencje Książki Pakiet relokacyjny Pomoc z wizą Pieniądze na koszty przeprowadzki Otwartość na pracowników z Ukrainy Udogodnienia w biurze Imprezy integracyjne Parking dla samochodów Parking dla rowerów Zimne napoje Gorące napoje Owoce Przekąski Lunche Prysznic Pokój relaksu Pokój zabaw dla dzieci Proces rekrutacji 1. Telefoniczna weryfikacja j. angielskiego (ok. 20 min.) 2. Rozmowa kwalifikacyjna (ok. 1,5-2 godz.) Power Media Gdańsk 160 Jesteśmy informatyczną spółką giełdową specjalizującą się w tworzeniu oprogramowania oraz rekrutacji i outsourcingu kadr IT. Prowadzimy również platformę księgowości internetowej ifirma.pl. Dla naszych klientów rekrutujemy głównie specjalistów z obszaru informatyki, telekomunikacji i elektroniki. Nr wpisu do Rejestru Agencji Zatrudnienia: 1264. Oferty pracy 32Profil firmy Power Media Senior Java Developer Aplikuj Znamy widełki Sprawdź, czy oferta pasuje do Twoich oczekiwań Ważna jeszcze 0 dni 11.10.2023 Doświadczenie Senior Typ współpracy Pełny etat Rodzaj umowy Umowa o pracę Praca zdalna 70% czasu Lokalizacja Gdańsk",
    job_description2 = "Samsung R&D Institute Poland Junior Telecommunication Test Engineer What you will do We are looking for candidates who are open to the possibility of expanding knowledge in the field of telecommunications. If you are curious in new challenges to the growing test team of working with live telecommunication network, global business trips and working in the international environment. Let us challenge you as a Junior Telecommunication Test engineer. Role and Responsibilities Mobile Equipment Field Tests (smartphones, wearable devices) Writing technical reports based on field tests results Cooperation with R&D centers around the world Technologies in use Latest telecommunication technologies (actually 5G and 4G+) Windows Atlassian tools (JIRA, Confluence) qTest Manger What we expect Skills and Qualifications Testing/QA certifications ISTQB/ITIL/ISEB Technical knowledge: telecommunication protocols Flexibility and willingness to travel - 20% of work time Last year of studies (Bachelor or Master degree in Physics, Mathematics, Electronics, Telecommunication or equivalent experience) Very good English verbal and written communication Good teamwork, communication skills Active driving license, category B Nice to have Analytical approach Good knowledge of 4G+, 5G technologies Experience with testing at least 1year How we work Laptop Additional monitor Headphones Personal container Windows Linux Benefits Packages and extras Healthcare package Healthcare package for families Leisure package Language courses Conferences Trainings Relocation package Money for moving expenses Amenities Bicycle parking Hot beverages Fruits Chill room Integration events Snacks Recruitment process Tech interview HR interview Samsung R&D Institute Poland Warszawa 1500-2000 Samsung R&D Institute Poland jest jednym z największych centrów badawczo-rozwojowych w Polsce. Nasze biura ulokowane są w Warszawie i Krakowie. To w nich powstaje wysokiej jakości oprogramowanie dla produktów Samsung Electronics. Pracujemy w międzynarodowym środowisku. Współpracujemy ze spółkami zależnymi w Europie, USA i w Azji. Praca naszych inżynierów wpływa na przyszłość działania m.in. flagowych modeli smartfonów i telewizorów, sieci mobilnych, multimediów, produktów AGD, robotów czy inteligentnych budynków. Nasz zespół składa się z ekspertów z wielu specjalistycznych obszarów. Wspólnie tworzymy środowisko, w którym możemy swobodnie dzielić się wiedzą i doświadczeniem. Pozostawiamy też przestrzeń do samodzielności, która sprzyja kreowaniu nowatorskich rozwiązań. Razem szukamy niestandardowych odpowiedzi, które pomagają nam tworzyć prawdziwe innowacje. Jeśli podzielasz naszą wiarę w siłę technologii, która zmienia rzeczywistość, pracujesz z pasją, masz w sobie ciekawość świata i ciągle chcesz się uczyć – to jest miejsce dla Ciebie, a my wiemy, jakie warunki pracy stworzyć, by sprzyjały Twojemu rozwojowi. Szukamy ludzi, którzy potrafią przekuć śmiałe wizje przyszłości w projekty i produkty, które będą służyć milionom ludzi na całym świecie. Job offers 25Company profile Samsung R&D Institute Poland Junior Telecommunication Test Engineer Apply Known salary brackets See if this offer matches your expectations Valid for 0 days 11.10.2023 Experience Junior Employment Type Full-time Contract type Employment contract Paid holidays 20/26 days per year Location Warsaw Plac Europejski 1"
    response1 = get_response(job_description1)
    response2 = get_response(job_description2)
    print(response1)
    print(response2)
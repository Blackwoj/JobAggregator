import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("LLAMA_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
headers = {"Authorization": f'Bearer {api_key}'}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

CLASSIFICATION_LABELS = ['job title', 'company name', 'location', 'job-type', 'technologies', 'salary', 'requirements']

job_description = "Power Media Senior Java Developer Co będziesz robić Klient: Międzynarodowy software house, zajmujący się realizacją projektów na potrzeby własne oraz swoich klientów. Jest liderem w zakresie doradztwa, transformacji cyfrowej oraz dostarczania nowoczesnych rozwiązań technologicznych oraz realizuje wiele różnorodnych projektów m.in dla światowych liderów z branży motoryzacyjnej, handlowej, dystrybucyjnej, telekomunikacyjnej i publicznej. Lokalizacja biura: Gdańsk (dzielnica Przymorze, okolice stacji kolejowej Gdańsk Oliwia). Hybrydowy model pracy: 70% zdalnie, 30% z biura. Główne technologie wykorzystywane w projektach: Java, Spring Boot, Spring, Hibernate, AWS, SQL, Oracle. Firma realizuje wiele różnorodnych projektów i na etapie rozmów dopasowuje pod kątem predyspozycji, doświadczenia, zainteresowań i zapotrzebowania projektowego. Zespoły projektowe są międzynarodowe, składają się z Developerów, Analityków, Testerów, Scrum Masterów, Project Managerów. Współpracują głównie z klientami z Niemiec, Holandii, Szwajcarii, USA. Kilka wybranych projektów: 1) Logistyka/transport: automatyzacja obsługi transportu morskiego i powietrznego, projekt długoterminowy, 70% development, 30% utrzymanie, ok. 30 osób w zespole z Polski. 2) Logistyka/transport: organizacja transportu morskiego oraz lotniczego, bardzo duży projekt, długoterminowy, 50% utrzymanie, 50% development. 3) Automotive: 100% development, ok. 50 osobowy zespół (Polska, Niemcy, Indie, Portugalia). Stack technologiczny: Java, Quarkus, PostgreSQL, Angular, Kubernetes. 4) Public: aplikacja, system umożliwiający składanie wniosków online, projekt długoterminowy, 80% development, 20% utrzymanie. Jako Senior Java Developer będziesz budować i rozwijać systemy mające bezpośredni wpływ na architekturę i rozwiązania technologiczne wykorzystywane w oprogramowaniach dla światowych liderów z branży motoryzacyjnej, handlowej, dystrybucyjnej, telekomunikacyjnej i publicznej. Będziesz miał okazje rozwijać się w obszarze One Click Deployment, Clean Code, Behavior Driven Development, Automation First itp. Zakres obowiązków: tworzenie nowoczesnych aplikacji opartych o technologie Java, tworzenie rozwiązań w oparciu o wzorce projektowe i architektoniczne wykorzystując podejścia: DevOps, Domain-Driven Design, Behavior-Driven Development, TDD oraz „Infrastructure as a Service/Code”, praca z wykorzystaniem z naszych z najlepszych praktyk i metodyk zwinnych (np. Scrum, SAFe, Kanban), rozwój w obszarze profesjonalnego wytwarzania oprogramowania, Clean Code itp., ścisła współpraca z doświadczonymi ekspertami, co umożliwia szerokie możliwości pogłębiania wiedzy technicznej, biznesowej oraz umiejętności interpersonalnych. Czego oczekujemy Główne wymagania: min. 6 lat doświadczenia związanego z programowaniem w języku Java praktyczne doświadczenie z: JEE, Spring Boot, Hibernate, znajomość zasad SOLID przy tworzeniu kodu (zasada CLEAN CODE) znajomość testów jednostkowych znajomość technologii: Java 8+, Maven, Unix, Linux, Github, Bitbucket doświadczenie w projektowaniu interfejsów REST API i wdrażaniu usług RESTful doświadczenie w projektowaniu baz danych z wykorzystaniem SQL, Oracle/SQL Server, Redis; bardzo dobra znajomość języka angielskiego (min. B2). Mile widziane: znajomość technologii frontendowych: JavaScript, TypeScript, Angular, React, Vue. Jak pracujemy Code review Baza wiedzy Testy jednostkowe Automatyzacja testów Laptop Komputer stacjonarny Dodatkowy monitor Słuchawki Osobista szafka Metodyka: Scrum Możliwość zmiany projektu Benefity Pakiety i dofinansowania Pakiet medyczny Kursy językowe Szkolenia Pakiet medyczny dla rodziny Pakiet sportowy Pakiet sportowy dla rodziny Konferencje Książki Pakiet relokacyjny Pomoc z wizą Pieniądze na koszty przeprowadzki Otwartość na pracowników z Ukrainy Udogodnienia w biurze Imprezy integracyjne Parking dla samochodów Parking dla rowerów Zimne napoje Gorące napoje Owoce Przekąski Lunche Prysznic Pokój relaksu Pokój zabaw dla dzieci Proces rekrutacji 1. Telefoniczna weryfikacja j. angielskiego (ok. 20 min.) 2. Rozmowa kwalifikacyjna (ok. 1,5-2 godz.) Power Media Gdańsk 160 Jesteśmy informatyczną spółką giełdową specjalizującą się w tworzeniu oprogramowania oraz rekrutacji i outsourcingu kadr IT. Prowadzimy również platformę księgowości internetowej ifirma.pl. Dla naszych klientów rekrutujemy głównie specjalistów z obszaru informatyki, telekomunikacji i elektroniki. Nr wpisu do Rejestru Agencji Zatrudnienia: 1264. Oferty pracy 32Profil firmy Power Media Senior Java Developer Aplikuj Znamy widełki Sprawdź, czy oferta pasuje do Twoich oczekiwań Ważna jeszcze 0 dni 11.10.2023 Doświadczenie Senior Typ współpracy Pełny etat Rodzaj umowy Umowa o pracę Praca zdalna 70% czasu Lokalizacja Gdańsk",
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

print(final_prompt)
print(output[0]['generated_text'])
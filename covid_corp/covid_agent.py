from allennlp.predictors.predictor import Predictor as AllenNLPPredictor


class Covid_agent:
    def __init__(self):
        self.predictor = AllenNLPPredictor.from_path(
            "https://storage.googleapis.com/allennlp-public-models/bidaf-elmo-model-2020.03.19.tar.gz",
            cuda_device=torch.cuda.current_device()
        )
        para = []
        para.append("There are many types of human coronaviruses including some that commonly cause mild upper-respiratory tract illnesses. COVID-19 is a new disease caused by a new coronavirus that has not previously been seen in humans.")
        para.append("Current understanding about how the virus that causes COVID-19 spreads is largely based on what is known about similar coronaviruses. COVID-19 is a new disease and there is more to learn about how it spreads, the severity of illness it causes, and to what extent it may spread in the United States.")
        para.append("People with COVID-19 have had a wide range of reported symptoms – ranging from mild symptoms to severe illness.")
        para.append("If you think you have been exposed to COVID-19 and develop a fever and symptoms of respiratory illness, such as cough or difficulty breathing, call your healthcare provider immediately. To help prevent the disease from spreading to people in your home and community, follow these CDC recommendations. We also recommend the use of LiveHealth Online, as well as care received from other providers delivering telehealth, as a safe and helpful way to use Empire benefits to see a doctor to receive health guidance related to COVID-19 without leaving home using your smart phone, tablet or computer-enabled web cam.")
        para.append("The best way to prevent infection is to avoid being exposed to the virus that causes COVID-19. Avoid close contac Avoid close contact with people who are sick. Stay home as much as possible. Put distance between yourself and other people. Keeping distance from others is especially important for people who are at higher risk of getting very sick. Practice good health habits. Everyday preventive actions help to prevent the spread of respiratory viruses. If soap and water are not readily available, use an alcohol-based hand sanitizer with at least 60 percent alcohol. Always wash hands with soap and water if hands are visibly dirty. Wash your hands often with soap and water for at least 20 seconds, especially after going to the bathroom; before eating; and after blowing your nose, coughing, or sneezing. Avoid close contact with people who are sick. Avoid touching your eyes, nose, and mouth. Stay home when you are sick. Cover your cough or sneeze with a tissue, then throw the tissue in the trash. Clean and disinfect frequently touched objects and surfaces using a regular household cleaning spray or wipe. Cover your mouth and nose with a cloth face when around others. Follow CDC’s recommendations for using a face cloth cover.")
        para.append("It’s best to follow the CDC’s recommendations on how to protect yourself, including who should wear cloth covers and when. Also, it’s important to know who should take extra precautions.")
        para.append("Members should call their provider to see how to get tested.")
        para.append("On May 1, 2020, the Food & Drug Administration issued an Emergency Use Authorization (EUA) for the antiviral drug remdesivir. While this EUA does not constitute an approval of this drug for the treatment of COVID-19, it does authorize the emergency use of the drug, as part of the current public health crisis, for the treatment of COVID-19 in patients meeting specific clinical criteria identified by the FDA. On March 28, 2020, the Food & Drug Administration issued an Emergency Use Authorization for the anti-malaria drugs chloroquine and hydroxychloroquine. While this EUA does not constitute an approval of this drug for the treatment of COVID-19, it does authorize the emergency use of the drug, as part of the current public health crisis, for the treatment of COVID-19 in patients meeting specific clinical criteria identified by the FDA. Neither of these drugs have received FDA approval for the treatment of COVID-19 and many are still being investigated. We are monitoring developments in this area closely and will evaluate coverage of any treatments once approved.")
        para.append("At the present time, no. Reports indicate there are several vaccines being evaluated but they are still in early stage development and have not been through clinical trials.")
        para.append("COVID-19 may be suspected when a person has symptoms consistent with COVID- 19, such as fever, cough or difficulty breathing, especially if there are risk factors for exposure to COVID-19, such as close contact with a confirmed COVID-19 patient or travel from affected geographic areas. A diagnosis is confirmed when other causes of respiratory disease, such as the flu, have been excluded, and a laboratory test has detected SARS-CoV-2, the virus that causes COVID-19. Other tests can help determine whether you have been exposed to SARS-CoV-2 (serology tests); these tests should be used to aid in the diagnosis of COVID-19 in conjunction with a medical review of symptoms and results of other laboratory tests.")
        para.append("Patients provide test samples in the doctor’s office, emergency room or hospital. Some areas may also have drive-through COVID-19 testing sites. There, swabs from patients’ nose, (and possibly mucus for those with a cough), will be collected and sent to a special lab to test for SARS-CoV-2, the virus that causes COVID-19. The specimens should be kept cold (2-8°C) and should generally be sent to a lab within three days. A blood (serology) test can also help determine whether you have been exposed to SARS-CoV-2. These tests should be used to aid in the diagnosis of COVID-19 in conjunction with a medical review of symptoms and results of other laboratory tests.")
        para.append("Clinicians should use their judgment to determine if a patient has signs and symptoms compatible with COVID-19 and whether the patient should be tested. While the CDC notes that clinicians are encouraged to test for other causes of respiratory illness, including infections such as influenza, in most cases, only a few other virus types require consideration (for example, influenza A and B with or without Respiratory Syncytial Virus). In most cases, it is unnecessary to test for more than five pathogen types in the specific patient being tested.")
        para.append("Empire is committed to help our members gain timely access to care and services. Our actions should help reduce barriers to seeing a doctor, getting tested and receiving treatment. Empire is waiving: cost-sharing for the treatment of COVID-19 by in-network providers from April 1 through Dec. 31, 2020 for members of its fully-insured employer, Individual, Medicare Advantage and Medicaid plans. This includes FDA-approved medications for the treatment of COVID-19 when they become available. We encourage our self-funded customers to participate and these plans will have an opportunity to opt in. cost-sharing for COVID-19 diagnostic tests, including serology or antibody tests, for members of our employer-sponsored, Individual, Medicare and Medicaid plans. This is effective throughout the duration of the public emergency. cost-sharing for COVID-19 screening related tests (e.g., influenza tests, blood tests, etc.) performed during a provider visit that results in an order for, or administration of, diagnostic testing for COVID-19 will also be covered with no cost sharing for members. This is effective throughout the duration of the public emergency. cost-sharing for visits to get the COVID-19 diagnostic test, regardless of whether the test is administered, beginning March 18 for members of our employer-sponsored, individual, Medicare and Medicaid plans. This is effective throughout the duration of the public emergency. cost-sharing for telehealth visits from in-network providers from March 17 through Sept. 30, 2020, including visits for behavioral health, for our fully- insured employer, individual, and Medicare Advantage plans, and where permissible, Medicaid plans. We encourage our self-funded customers to participate, although these plans will have an opportunity to opt in. cost-sharing for FDA-approved vaccines when they become available. The cost-sharing waiver includes copays, coinsurance and deductibles. For additional services, members will pay any cost sharing their plan requires, unless otherwise determined by state law or regulation. Members can call the number on the back of their identification card to confirm coverage. Providers should continue to verify eligibility and benefits for all members prior to rendering services.")
        
        self.corpus = ''.join(para)

    def answer(self, question):
        prediction = self.predictor.predict(
            passage = self.corpus, question= question
        )
        [start, end] = prediction['best_span']
        line = find_beginning_end(start, end, self.corpus)
        return prediction["best_span_str"], line  
    
    def get_corpus(self):
        return self.corpus
    
def find_new_line_backward(start, end, text):
    if end == 0:
        end = start + 1
    start -= 1     # start backing up the document
    partial_str = text[start: end]
#     print('partial_str={}'.format(partial_str))
    start_index = -1
    try:
        start_index = re.search("\n\n", partial_str).start()
    except:
        pass
#     print('start_index= {}'.format(start_index))
    while start_index != 0:
        start -= 1
        partial_str = text[start: end]
#         print('partial_str={}'.format(partial_str))
        try:
            start_index = re.search("\n\n", partial_str).start()
        except:
            pass
#         print('start_index= {}'.format(start_index))
    
#     print('final start_index= {}'.format(start))
    return start

def find_new_line_forward(start, end, text):
    end += 1     # start backing up the document
    partial_str = text[start: end]
#     print('partial_str={}'.format(partial_str))
    end_index = -1
    try:
        end_index = re.search("\n\n", partial_str).start()
    except:
        pass
#     print('start_index= {}'.format(start_index))
    while end_index == -1:
        end += 1
        partial_str = text[start: end]
#         print('partial_str={}'.format(partial_str))
        try:
            end_index = re.search("\n\n", partial_str).start()
        except:
            pass
#         print('end_index= {}'.format(end_index))
    
#     print('final end_index= {}'.format(start))
    return end

def find_beginning_end(start, end, text):
    line_start = find_new_line_backward(start, end, text)
    line_end = find_new_line_forward(start, end, text)
    line = text[line_start + 2: line_end - 2]
#     print('before sub line={}'.format(line))
    line = re.sub('[*]+', '', line)
    line = line.strip()
#     print('after sub line={}'.format(line))
    return line


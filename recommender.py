# check result of mbti
import json


def recommender_ai(result_):
    global mbti_result
    if result_ == "ISTJ":
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "A Logistician is someone with the Introverted, Observant, Thinking, and Judging personality traits. These people tend to be reserved yet willful, with a rational outlook on life. They compose their actions carefully and carry them out with methodical purpose.",
           "Recommend Jobs and Activities" : "Dentist, Certified public accountant, Supply chain manager, Business analyst"
        }
        mbti_result = json.dumps(mbti_result)
    elif result_ == 'ISFJ':
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "A Defender is someone with the Introverted, Observant, Feeling, and Judging personality traits. These people tend to be warm and unassuming in their own steady way. They’re efficient and responsible, giving careful attention to practical details in their daily lives.",
           "Recommend Jobs and Activities" : "Accountant, Financial clerk, Bank teller, Research analyst, Accountant, Administrative manager, Photographer, Elementary teacher"
        }
    elif result_ == 'INFJ':
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "An Advocate is someone with the Introverted, Intuitive, Feeling, and Judging personality traits. They tend to approach life with deep thoughtfulness and imagination. Their inner vision, personal values, and a quiet, principled version of humanism guide them in all things.",
           "Recommend Jobs and Activities" : "Counselor, Writer, Scientist, Librarian,Psychologist"
        }
        mbti_result = json.dumps(mbti_result)
    elif result_ == 'INTJ':
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "An Architect is a person with the Introverted, Intuitive, Thinking, and Judging personality traits. These thoughtful tacticians love perfecting the details of life, applying creativity and rationality to everything they do. Their inner world is often a private, complex one.",
           "Recommend Jobs and Activities" : """Musical performer, Managing editor, Photographer, Financial advisor, Marketing manager, Teacher, Physical therapist.I work in the social services in a very front-line role. Although I want to get into more of the planning and organizing side of the social services I do enjoy my job for the most part now. It's a fun challenge when someone comes in because I get to assess their needs and put the puzzle pieces together by connecting that client with appropriate resources or services.
There are some aspects of working for a non-profit that really suit INTJ's and others that don't. I have a decent amount of control and say into how things are run. I can often develop new workshops or make suggestions for how my agency should change programming and I'm fairly new to the field. But I spend a lot of time completing mundane, redundant tasks that drive me insane because I don't feel the need to just accept every request funders give my agency."""
        }
        mbti_result = json.dumps(mbti_result)
    elif result_ == 'ISTP':
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "A Virtuoso is someone with the Introverted, Observant, Thinking, and Prospecting personality traits. They tend to have an individualistic mindset, pursuing goals without needing much external connection. They engage in life with inquisitiveness and personal skill, varying their approach as needed.",
           "Recommend Jobs and Activities" : "Technician, Construction worker, Engineer, Forensic scientist, Inspector"
        }
        mbti_result = json.dumps(mbti_result)
    elif result_ == 'ISFP':
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "An Adventurer is a person with the Introverted, Observant, Feeling, and Prospecting personality traits. They tend to have open minds, approaching life, new experiences, and people with grounded warmth. Their ability to stay in the moment helps them uncover exciting potentials.",
           "Recommend Jobs and Activities" : "Bookkeeper, Social media manager, Optician, Veterinarian, Archeologist, Social worker, Occupational therapist"
        }
        mbti_result = json.dumps(mbti_result)
    elif result_ == 'INFP':
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "A Mediator is someone who possesses the Introverted, Intuitive, Feeling, and Prospecting personality traits. These rare personality types tend to be quiet, open-minded, and imaginative, and they apply a caring and creative approach to everything they do.",
           "Recommend Jobs and Activities" : "Copywriter, HR manager, Physical therapist, Mental health professional, Artist, Photographer"
        }
        mbti_result = json.dumps(mbti_result)
    elif result_ == 'INTP':
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "A Logician is someone with the Introverted, Intuitive, Thinking, and Prospecting personality traits. These flexible thinkers enjoy taking an unconventional approach to many aspects of life. They often seek out unlikely paths, mixing willingness to experiment with personal creativity.",
           "Recommend Jobs and Activities" : "Composer, Professor, Writer, Producer, Biomedical engineer, Marketing consultant, Web developer"
        }
        mbti_result = json.dumps(mbti_result)
    elif result_ == 'ESTP':
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "An Entrepreneur is someone with the Extraverted, Observant, Thinking, and Prospecting personality traits. They tend to be energetic and action-oriented, deftly navigating whatever is in front of them. They love uncovering life’s opportunities, whether socializing with others or in more personal pursuits.",
           "Recommend Jobs and Activities" : "Firefighter, Paramedic, Creative director, Project coordinator, Construction manager"
        }
        mbti_result = json.dumps(mbti_result)
    elif result_ == 'ESFP':
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "An Entertainer is a person with the Extraverted, Observant, Feeling, and Prospecting personality traits. These people love vibrant experiences, engaging in life eagerly and taking pleasure in discovering the unknown. They can be very social, often encouraging others into shared activities.",
           "Recommend Jobs and Activities" : "Event planner, Professional entertainer, Sales representative, Cosmetologist, Flight attendant, Tour guide"
        }
        mbti_result = json.dumps(mbti_result)
    elif result_ == 'ENFP':
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "The ENFP personality type is highly individualistic. These people strive towards creating their own looks, methods, actions, habits and ideas. They dislike being forced to live inside a box. They have a strong intuitive nature and like being around others. They are highly perceptive and operate from their feelings most of the time. ENFPs are drawn to more casual work environments. They are motivated more by goals that they are passionate about rather than money. Careers that are ideal for ENFPs include",
           "Recommend Jobs and Activities" : "Reporter or news anchor, Editor, Musician, Product manager, Elementary school teacher, Personal trainer, Social worker"
        }
        mbti_result = json.dumps(mbti_result)
    elif result_ == 'ENTP':
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "A Debater is a person with the Extraverted, Intuitive, Thinking, and Prospecting personality traits. They tend to be bold and creative, deconstructing and rebuilding ideas with great mental agility. They pursue their goals vigorously despite any resistance they might encounter.",
           "Recommend Jobs and Activities" : "Attorney, Copywriter, Financial planner, Psychologist, Systems analyst, Creative director, Operations specialist"
        }
        mbti_result = json.dumps(mbti_result)
    elif result_ == 'ESTJ':
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "An Executive is someone with the Extraverted, Observant, Thinking, and Judging personality traits. They possess great fortitude, emphatically following their own sensible judgment. They often serve as a stabilizing force among others, able to offer solid direction amid adversity.",
           "Recommend Jobs and Activities" : "Judge, Coach, Financial officer, Hotel manager, Real estate agent"
        }
        mbti_result = json.dumps(mbti_result)
    elif result_ == 'ENFJ':
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "A Protagonist is a person with the Extraverted, Intuitive, Feeling, and Judging personality traits. These warm, forthright types love helping others, and they tend to have strong ideas and values. They back their perspective with the creative energy to achieve their goals.",
           "Recommend Jobs and Activities" : "Guidance counselor, Sales manager, HR director, Art director,Public relations manager"
        }
        mbti_result = json.dumps(mbti_result)
    elif result_ == 'ENTJ': #entj
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "A Commander is someone with the Extraverted, Intuitive, Thinking, and Judging personality traits. They are decisive people who love momentum and accomplishment. They gather information to construct their creative visions but rarely hesitate for long before acting on them.",
           "Recommend Jobs and Activities" : "Business administrator, Public relations specialist, Mechanical engineer, Judge, Construction manager, Astronomer"
        }
        mbti_result = json.dumps(mbti_result)
    elif result_ == 'ESFJ':
        mbti_result = {
           "MBTI results analyzed based on cover letter" : "A Consul is a person with the Extraverted, Observant, Feeling, and Judging personality traits. They are attentive and people-focused, and they enjoy taking part in their social community. Their achievements are guided by decisive values, and they willingly offer guidance to others.",
           "Recommend Jobs and Activities" : "Office manager, Technical support specialist, Museum curator, Psychologist, Medical researcher"
        }
        mbti_result = json.dumps(mbti_result)
    else:
        mbti_result = {
           "MBTI results analyzed based on cover letter": "Try Aagin"
        }
        mbti_result = json.dumps(mbti_result)
    
    return mbti_result

# search activity from act_db

# get result of the searched actvity
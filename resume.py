from Alchemy import banco

class ResumeModel(banco.Model): 
    
    __tablename__ = 'resumes'
    id = banco.Column(banco.Integer, primary_key = True)
    experiences = banco.relationship('experienceModel', back_populates="resumes")
    
    
    
    def __init__(self, id, experience, education, skills, languages, objective):
        self.id = id
        self.experience = experience
        self.education = education
        self.skills = skills
        self.languages = languages
        self.objective = objective



class ExperienceModel(): 
    __tablename__ = 'experiences'
    id = banco.Column(banco.Integer, primary_key = True)
    resume_id = banco.Column(banco.Integer, ForeignKey('resumes.id'))
    resume = relationship("ResumeModel", back_populates = 'experiences')
    title = banco.Column(banco.String(80))
    descricao = banco.Column(banco.String(400))
    start_date = banco.Column(banco.Date)
    end_date = banco.Column(banco.Date)

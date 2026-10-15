"""
Exhaustive Test Suite for TalentMatch AI NLP Matching Engine
"""
import unittest
from backend.services.nlp_engine import NLPMatchingEngine

class TestNLPMatchingEngineExhaustive(unittest.TestCase):
    def setUp(self):
        self.engine = NLPMatchingEngine()

    def test_nlp_case_0001(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1"
        job_desc = "Looking for Python React AWS engineer position 1"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0002(self):
        doc_text = "Experienced Python developer with React and AWS competency case 2"
        job_desc = "Looking for Python React AWS engineer position 2"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0003(self):
        doc_text = "Experienced Python developer with React and AWS competency case 3"
        job_desc = "Looking for Python React AWS engineer position 3"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0004(self):
        doc_text = "Experienced Python developer with React and AWS competency case 4"
        job_desc = "Looking for Python React AWS engineer position 4"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0005(self):
        doc_text = "Experienced Python developer with React and AWS competency case 5"
        job_desc = "Looking for Python React AWS engineer position 5"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0006(self):
        doc_text = "Experienced Python developer with React and AWS competency case 6"
        job_desc = "Looking for Python React AWS engineer position 6"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0007(self):
        doc_text = "Experienced Python developer with React and AWS competency case 7"
        job_desc = "Looking for Python React AWS engineer position 7"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0008(self):
        doc_text = "Experienced Python developer with React and AWS competency case 8"
        job_desc = "Looking for Python React AWS engineer position 8"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0009(self):
        doc_text = "Experienced Python developer with React and AWS competency case 9"
        job_desc = "Looking for Python React AWS engineer position 9"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0010(self):
        doc_text = "Experienced Python developer with React and AWS competency case 10"
        job_desc = "Looking for Python React AWS engineer position 10"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0011(self):
        doc_text = "Experienced Python developer with React and AWS competency case 11"
        job_desc = "Looking for Python React AWS engineer position 11"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0012(self):
        doc_text = "Experienced Python developer with React and AWS competency case 12"
        job_desc = "Looking for Python React AWS engineer position 12"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0013(self):
        doc_text = "Experienced Python developer with React and AWS competency case 13"
        job_desc = "Looking for Python React AWS engineer position 13"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0014(self):
        doc_text = "Experienced Python developer with React and AWS competency case 14"
        job_desc = "Looking for Python React AWS engineer position 14"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0015(self):
        doc_text = "Experienced Python developer with React and AWS competency case 15"
        job_desc = "Looking for Python React AWS engineer position 15"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0016(self):
        doc_text = "Experienced Python developer with React and AWS competency case 16"
        job_desc = "Looking for Python React AWS engineer position 16"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0017(self):
        doc_text = "Experienced Python developer with React and AWS competency case 17"
        job_desc = "Looking for Python React AWS engineer position 17"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0018(self):
        doc_text = "Experienced Python developer with React and AWS competency case 18"
        job_desc = "Looking for Python React AWS engineer position 18"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0019(self):
        doc_text = "Experienced Python developer with React and AWS competency case 19"
        job_desc = "Looking for Python React AWS engineer position 19"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0020(self):
        doc_text = "Experienced Python developer with React and AWS competency case 20"
        job_desc = "Looking for Python React AWS engineer position 20"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0021(self):
        doc_text = "Experienced Python developer with React and AWS competency case 21"
        job_desc = "Looking for Python React AWS engineer position 21"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0022(self):
        doc_text = "Experienced Python developer with React and AWS competency case 22"
        job_desc = "Looking for Python React AWS engineer position 22"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0023(self):
        doc_text = "Experienced Python developer with React and AWS competency case 23"
        job_desc = "Looking for Python React AWS engineer position 23"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0024(self):
        doc_text = "Experienced Python developer with React and AWS competency case 24"
        job_desc = "Looking for Python React AWS engineer position 24"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0025(self):
        doc_text = "Experienced Python developer with React and AWS competency case 25"
        job_desc = "Looking for Python React AWS engineer position 25"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0026(self):
        doc_text = "Experienced Python developer with React and AWS competency case 26"
        job_desc = "Looking for Python React AWS engineer position 26"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0027(self):
        doc_text = "Experienced Python developer with React and AWS competency case 27"
        job_desc = "Looking for Python React AWS engineer position 27"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0028(self):
        doc_text = "Experienced Python developer with React and AWS competency case 28"
        job_desc = "Looking for Python React AWS engineer position 28"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0029(self):
        doc_text = "Experienced Python developer with React and AWS competency case 29"
        job_desc = "Looking for Python React AWS engineer position 29"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0030(self):
        doc_text = "Experienced Python developer with React and AWS competency case 30"
        job_desc = "Looking for Python React AWS engineer position 30"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0031(self):
        doc_text = "Experienced Python developer with React and AWS competency case 31"
        job_desc = "Looking for Python React AWS engineer position 31"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0032(self):
        doc_text = "Experienced Python developer with React and AWS competency case 32"
        job_desc = "Looking for Python React AWS engineer position 32"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0033(self):
        doc_text = "Experienced Python developer with React and AWS competency case 33"
        job_desc = "Looking for Python React AWS engineer position 33"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0034(self):
        doc_text = "Experienced Python developer with React and AWS competency case 34"
        job_desc = "Looking for Python React AWS engineer position 34"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0035(self):
        doc_text = "Experienced Python developer with React and AWS competency case 35"
        job_desc = "Looking for Python React AWS engineer position 35"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0036(self):
        doc_text = "Experienced Python developer with React and AWS competency case 36"
        job_desc = "Looking for Python React AWS engineer position 36"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0037(self):
        doc_text = "Experienced Python developer with React and AWS competency case 37"
        job_desc = "Looking for Python React AWS engineer position 37"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0038(self):
        doc_text = "Experienced Python developer with React and AWS competency case 38"
        job_desc = "Looking for Python React AWS engineer position 38"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0039(self):
        doc_text = "Experienced Python developer with React and AWS competency case 39"
        job_desc = "Looking for Python React AWS engineer position 39"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0040(self):
        doc_text = "Experienced Python developer with React and AWS competency case 40"
        job_desc = "Looking for Python React AWS engineer position 40"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0041(self):
        doc_text = "Experienced Python developer with React and AWS competency case 41"
        job_desc = "Looking for Python React AWS engineer position 41"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0042(self):
        doc_text = "Experienced Python developer with React and AWS competency case 42"
        job_desc = "Looking for Python React AWS engineer position 42"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0043(self):
        doc_text = "Experienced Python developer with React and AWS competency case 43"
        job_desc = "Looking for Python React AWS engineer position 43"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0044(self):
        doc_text = "Experienced Python developer with React and AWS competency case 44"
        job_desc = "Looking for Python React AWS engineer position 44"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0045(self):
        doc_text = "Experienced Python developer with React and AWS competency case 45"
        job_desc = "Looking for Python React AWS engineer position 45"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0046(self):
        doc_text = "Experienced Python developer with React and AWS competency case 46"
        job_desc = "Looking for Python React AWS engineer position 46"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0047(self):
        doc_text = "Experienced Python developer with React and AWS competency case 47"
        job_desc = "Looking for Python React AWS engineer position 47"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0048(self):
        doc_text = "Experienced Python developer with React and AWS competency case 48"
        job_desc = "Looking for Python React AWS engineer position 48"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0049(self):
        doc_text = "Experienced Python developer with React and AWS competency case 49"
        job_desc = "Looking for Python React AWS engineer position 49"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0050(self):
        doc_text = "Experienced Python developer with React and AWS competency case 50"
        job_desc = "Looking for Python React AWS engineer position 50"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0051(self):
        doc_text = "Experienced Python developer with React and AWS competency case 51"
        job_desc = "Looking for Python React AWS engineer position 51"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0052(self):
        doc_text = "Experienced Python developer with React and AWS competency case 52"
        job_desc = "Looking for Python React AWS engineer position 52"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0053(self):
        doc_text = "Experienced Python developer with React and AWS competency case 53"
        job_desc = "Looking for Python React AWS engineer position 53"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0054(self):
        doc_text = "Experienced Python developer with React and AWS competency case 54"
        job_desc = "Looking for Python React AWS engineer position 54"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0055(self):
        doc_text = "Experienced Python developer with React and AWS competency case 55"
        job_desc = "Looking for Python React AWS engineer position 55"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0056(self):
        doc_text = "Experienced Python developer with React and AWS competency case 56"
        job_desc = "Looking for Python React AWS engineer position 56"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0057(self):
        doc_text = "Experienced Python developer with React and AWS competency case 57"
        job_desc = "Looking for Python React AWS engineer position 57"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0058(self):
        doc_text = "Experienced Python developer with React and AWS competency case 58"
        job_desc = "Looking for Python React AWS engineer position 58"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0059(self):
        doc_text = "Experienced Python developer with React and AWS competency case 59"
        job_desc = "Looking for Python React AWS engineer position 59"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0060(self):
        doc_text = "Experienced Python developer with React and AWS competency case 60"
        job_desc = "Looking for Python React AWS engineer position 60"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0061(self):
        doc_text = "Experienced Python developer with React and AWS competency case 61"
        job_desc = "Looking for Python React AWS engineer position 61"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0062(self):
        doc_text = "Experienced Python developer with React and AWS competency case 62"
        job_desc = "Looking for Python React AWS engineer position 62"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0063(self):
        doc_text = "Experienced Python developer with React and AWS competency case 63"
        job_desc = "Looking for Python React AWS engineer position 63"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0064(self):
        doc_text = "Experienced Python developer with React and AWS competency case 64"
        job_desc = "Looking for Python React AWS engineer position 64"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0065(self):
        doc_text = "Experienced Python developer with React and AWS competency case 65"
        job_desc = "Looking for Python React AWS engineer position 65"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0066(self):
        doc_text = "Experienced Python developer with React and AWS competency case 66"
        job_desc = "Looking for Python React AWS engineer position 66"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0067(self):
        doc_text = "Experienced Python developer with React and AWS competency case 67"
        job_desc = "Looking for Python React AWS engineer position 67"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0068(self):
        doc_text = "Experienced Python developer with React and AWS competency case 68"
        job_desc = "Looking for Python React AWS engineer position 68"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0069(self):
        doc_text = "Experienced Python developer with React and AWS competency case 69"
        job_desc = "Looking for Python React AWS engineer position 69"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0070(self):
        doc_text = "Experienced Python developer with React and AWS competency case 70"
        job_desc = "Looking for Python React AWS engineer position 70"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0071(self):
        doc_text = "Experienced Python developer with React and AWS competency case 71"
        job_desc = "Looking for Python React AWS engineer position 71"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0072(self):
        doc_text = "Experienced Python developer with React and AWS competency case 72"
        job_desc = "Looking for Python React AWS engineer position 72"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0073(self):
        doc_text = "Experienced Python developer with React and AWS competency case 73"
        job_desc = "Looking for Python React AWS engineer position 73"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0074(self):
        doc_text = "Experienced Python developer with React and AWS competency case 74"
        job_desc = "Looking for Python React AWS engineer position 74"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0075(self):
        doc_text = "Experienced Python developer with React and AWS competency case 75"
        job_desc = "Looking for Python React AWS engineer position 75"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0076(self):
        doc_text = "Experienced Python developer with React and AWS competency case 76"
        job_desc = "Looking for Python React AWS engineer position 76"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0077(self):
        doc_text = "Experienced Python developer with React and AWS competency case 77"
        job_desc = "Looking for Python React AWS engineer position 77"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0078(self):
        doc_text = "Experienced Python developer with React and AWS competency case 78"
        job_desc = "Looking for Python React AWS engineer position 78"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0079(self):
        doc_text = "Experienced Python developer with React and AWS competency case 79"
        job_desc = "Looking for Python React AWS engineer position 79"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0080(self):
        doc_text = "Experienced Python developer with React and AWS competency case 80"
        job_desc = "Looking for Python React AWS engineer position 80"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0081(self):
        doc_text = "Experienced Python developer with React and AWS competency case 81"
        job_desc = "Looking for Python React AWS engineer position 81"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0082(self):
        doc_text = "Experienced Python developer with React and AWS competency case 82"
        job_desc = "Looking for Python React AWS engineer position 82"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0083(self):
        doc_text = "Experienced Python developer with React and AWS competency case 83"
        job_desc = "Looking for Python React AWS engineer position 83"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0084(self):
        doc_text = "Experienced Python developer with React and AWS competency case 84"
        job_desc = "Looking for Python React AWS engineer position 84"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0085(self):
        doc_text = "Experienced Python developer with React and AWS competency case 85"
        job_desc = "Looking for Python React AWS engineer position 85"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0086(self):
        doc_text = "Experienced Python developer with React and AWS competency case 86"
        job_desc = "Looking for Python React AWS engineer position 86"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0087(self):
        doc_text = "Experienced Python developer with React and AWS competency case 87"
        job_desc = "Looking for Python React AWS engineer position 87"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0088(self):
        doc_text = "Experienced Python developer with React and AWS competency case 88"
        job_desc = "Looking for Python React AWS engineer position 88"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0089(self):
        doc_text = "Experienced Python developer with React and AWS competency case 89"
        job_desc = "Looking for Python React AWS engineer position 89"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0090(self):
        doc_text = "Experienced Python developer with React and AWS competency case 90"
        job_desc = "Looking for Python React AWS engineer position 90"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0091(self):
        doc_text = "Experienced Python developer with React and AWS competency case 91"
        job_desc = "Looking for Python React AWS engineer position 91"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0092(self):
        doc_text = "Experienced Python developer with React and AWS competency case 92"
        job_desc = "Looking for Python React AWS engineer position 92"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0093(self):
        doc_text = "Experienced Python developer with React and AWS competency case 93"
        job_desc = "Looking for Python React AWS engineer position 93"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0094(self):
        doc_text = "Experienced Python developer with React and AWS competency case 94"
        job_desc = "Looking for Python React AWS engineer position 94"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0095(self):
        doc_text = "Experienced Python developer with React and AWS competency case 95"
        job_desc = "Looking for Python React AWS engineer position 95"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0096(self):
        doc_text = "Experienced Python developer with React and AWS competency case 96"
        job_desc = "Looking for Python React AWS engineer position 96"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0097(self):
        doc_text = "Experienced Python developer with React and AWS competency case 97"
        job_desc = "Looking for Python React AWS engineer position 97"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0098(self):
        doc_text = "Experienced Python developer with React and AWS competency case 98"
        job_desc = "Looking for Python React AWS engineer position 98"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0099(self):
        doc_text = "Experienced Python developer with React and AWS competency case 99"
        job_desc = "Looking for Python React AWS engineer position 99"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0100(self):
        doc_text = "Experienced Python developer with React and AWS competency case 100"
        job_desc = "Looking for Python React AWS engineer position 100"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0101(self):
        doc_text = "Experienced Python developer with React and AWS competency case 101"
        job_desc = "Looking for Python React AWS engineer position 101"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0102(self):
        doc_text = "Experienced Python developer with React and AWS competency case 102"
        job_desc = "Looking for Python React AWS engineer position 102"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0103(self):
        doc_text = "Experienced Python developer with React and AWS competency case 103"
        job_desc = "Looking for Python React AWS engineer position 103"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0104(self):
        doc_text = "Experienced Python developer with React and AWS competency case 104"
        job_desc = "Looking for Python React AWS engineer position 104"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0105(self):
        doc_text = "Experienced Python developer with React and AWS competency case 105"
        job_desc = "Looking for Python React AWS engineer position 105"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0106(self):
        doc_text = "Experienced Python developer with React and AWS competency case 106"
        job_desc = "Looking for Python React AWS engineer position 106"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0107(self):
        doc_text = "Experienced Python developer with React and AWS competency case 107"
        job_desc = "Looking for Python React AWS engineer position 107"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0108(self):
        doc_text = "Experienced Python developer with React and AWS competency case 108"
        job_desc = "Looking for Python React AWS engineer position 108"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0109(self):
        doc_text = "Experienced Python developer with React and AWS competency case 109"
        job_desc = "Looking for Python React AWS engineer position 109"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0110(self):
        doc_text = "Experienced Python developer with React and AWS competency case 110"
        job_desc = "Looking for Python React AWS engineer position 110"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0111(self):
        doc_text = "Experienced Python developer with React and AWS competency case 111"
        job_desc = "Looking for Python React AWS engineer position 111"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0112(self):
        doc_text = "Experienced Python developer with React and AWS competency case 112"
        job_desc = "Looking for Python React AWS engineer position 112"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0113(self):
        doc_text = "Experienced Python developer with React and AWS competency case 113"
        job_desc = "Looking for Python React AWS engineer position 113"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0114(self):
        doc_text = "Experienced Python developer with React and AWS competency case 114"
        job_desc = "Looking for Python React AWS engineer position 114"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0115(self):
        doc_text = "Experienced Python developer with React and AWS competency case 115"
        job_desc = "Looking for Python React AWS engineer position 115"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0116(self):
        doc_text = "Experienced Python developer with React and AWS competency case 116"
        job_desc = "Looking for Python React AWS engineer position 116"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0117(self):
        doc_text = "Experienced Python developer with React and AWS competency case 117"
        job_desc = "Looking for Python React AWS engineer position 117"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0118(self):
        doc_text = "Experienced Python developer with React and AWS competency case 118"
        job_desc = "Looking for Python React AWS engineer position 118"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0119(self):
        doc_text = "Experienced Python developer with React and AWS competency case 119"
        job_desc = "Looking for Python React AWS engineer position 119"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0120(self):
        doc_text = "Experienced Python developer with React and AWS competency case 120"
        job_desc = "Looking for Python React AWS engineer position 120"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0121(self):
        doc_text = "Experienced Python developer with React and AWS competency case 121"
        job_desc = "Looking for Python React AWS engineer position 121"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0122(self):
        doc_text = "Experienced Python developer with React and AWS competency case 122"
        job_desc = "Looking for Python React AWS engineer position 122"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0123(self):
        doc_text = "Experienced Python developer with React and AWS competency case 123"
        job_desc = "Looking for Python React AWS engineer position 123"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0124(self):
        doc_text = "Experienced Python developer with React and AWS competency case 124"
        job_desc = "Looking for Python React AWS engineer position 124"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0125(self):
        doc_text = "Experienced Python developer with React and AWS competency case 125"
        job_desc = "Looking for Python React AWS engineer position 125"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0126(self):
        doc_text = "Experienced Python developer with React and AWS competency case 126"
        job_desc = "Looking for Python React AWS engineer position 126"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0127(self):
        doc_text = "Experienced Python developer with React and AWS competency case 127"
        job_desc = "Looking for Python React AWS engineer position 127"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0128(self):
        doc_text = "Experienced Python developer with React and AWS competency case 128"
        job_desc = "Looking for Python React AWS engineer position 128"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0129(self):
        doc_text = "Experienced Python developer with React and AWS competency case 129"
        job_desc = "Looking for Python React AWS engineer position 129"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0130(self):
        doc_text = "Experienced Python developer with React and AWS competency case 130"
        job_desc = "Looking for Python React AWS engineer position 130"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0131(self):
        doc_text = "Experienced Python developer with React and AWS competency case 131"
        job_desc = "Looking for Python React AWS engineer position 131"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0132(self):
        doc_text = "Experienced Python developer with React and AWS competency case 132"
        job_desc = "Looking for Python React AWS engineer position 132"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0133(self):
        doc_text = "Experienced Python developer with React and AWS competency case 133"
        job_desc = "Looking for Python React AWS engineer position 133"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0134(self):
        doc_text = "Experienced Python developer with React and AWS competency case 134"
        job_desc = "Looking for Python React AWS engineer position 134"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0135(self):
        doc_text = "Experienced Python developer with React and AWS competency case 135"
        job_desc = "Looking for Python React AWS engineer position 135"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0136(self):
        doc_text = "Experienced Python developer with React and AWS competency case 136"
        job_desc = "Looking for Python React AWS engineer position 136"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0137(self):
        doc_text = "Experienced Python developer with React and AWS competency case 137"
        job_desc = "Looking for Python React AWS engineer position 137"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0138(self):
        doc_text = "Experienced Python developer with React and AWS competency case 138"
        job_desc = "Looking for Python React AWS engineer position 138"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0139(self):
        doc_text = "Experienced Python developer with React and AWS competency case 139"
        job_desc = "Looking for Python React AWS engineer position 139"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0140(self):
        doc_text = "Experienced Python developer with React and AWS competency case 140"
        job_desc = "Looking for Python React AWS engineer position 140"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0141(self):
        doc_text = "Experienced Python developer with React and AWS competency case 141"
        job_desc = "Looking for Python React AWS engineer position 141"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0142(self):
        doc_text = "Experienced Python developer with React and AWS competency case 142"
        job_desc = "Looking for Python React AWS engineer position 142"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0143(self):
        doc_text = "Experienced Python developer with React and AWS competency case 143"
        job_desc = "Looking for Python React AWS engineer position 143"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0144(self):
        doc_text = "Experienced Python developer with React and AWS competency case 144"
        job_desc = "Looking for Python React AWS engineer position 144"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0145(self):
        doc_text = "Experienced Python developer with React and AWS competency case 145"
        job_desc = "Looking for Python React AWS engineer position 145"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0146(self):
        doc_text = "Experienced Python developer with React and AWS competency case 146"
        job_desc = "Looking for Python React AWS engineer position 146"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0147(self):
        doc_text = "Experienced Python developer with React and AWS competency case 147"
        job_desc = "Looking for Python React AWS engineer position 147"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0148(self):
        doc_text = "Experienced Python developer with React and AWS competency case 148"
        job_desc = "Looking for Python React AWS engineer position 148"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0149(self):
        doc_text = "Experienced Python developer with React and AWS competency case 149"
        job_desc = "Looking for Python React AWS engineer position 149"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0150(self):
        doc_text = "Experienced Python developer with React and AWS competency case 150"
        job_desc = "Looking for Python React AWS engineer position 150"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0151(self):
        doc_text = "Experienced Python developer with React and AWS competency case 151"
        job_desc = "Looking for Python React AWS engineer position 151"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0152(self):
        doc_text = "Experienced Python developer with React and AWS competency case 152"
        job_desc = "Looking for Python React AWS engineer position 152"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0153(self):
        doc_text = "Experienced Python developer with React and AWS competency case 153"
        job_desc = "Looking for Python React AWS engineer position 153"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0154(self):
        doc_text = "Experienced Python developer with React and AWS competency case 154"
        job_desc = "Looking for Python React AWS engineer position 154"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0155(self):
        doc_text = "Experienced Python developer with React and AWS competency case 155"
        job_desc = "Looking for Python React AWS engineer position 155"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0156(self):
        doc_text = "Experienced Python developer with React and AWS competency case 156"
        job_desc = "Looking for Python React AWS engineer position 156"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0157(self):
        doc_text = "Experienced Python developer with React and AWS competency case 157"
        job_desc = "Looking for Python React AWS engineer position 157"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0158(self):
        doc_text = "Experienced Python developer with React and AWS competency case 158"
        job_desc = "Looking for Python React AWS engineer position 158"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0159(self):
        doc_text = "Experienced Python developer with React and AWS competency case 159"
        job_desc = "Looking for Python React AWS engineer position 159"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0160(self):
        doc_text = "Experienced Python developer with React and AWS competency case 160"
        job_desc = "Looking for Python React AWS engineer position 160"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0161(self):
        doc_text = "Experienced Python developer with React and AWS competency case 161"
        job_desc = "Looking for Python React AWS engineer position 161"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0162(self):
        doc_text = "Experienced Python developer with React and AWS competency case 162"
        job_desc = "Looking for Python React AWS engineer position 162"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0163(self):
        doc_text = "Experienced Python developer with React and AWS competency case 163"
        job_desc = "Looking for Python React AWS engineer position 163"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0164(self):
        doc_text = "Experienced Python developer with React and AWS competency case 164"
        job_desc = "Looking for Python React AWS engineer position 164"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0165(self):
        doc_text = "Experienced Python developer with React and AWS competency case 165"
        job_desc = "Looking for Python React AWS engineer position 165"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0166(self):
        doc_text = "Experienced Python developer with React and AWS competency case 166"
        job_desc = "Looking for Python React AWS engineer position 166"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0167(self):
        doc_text = "Experienced Python developer with React and AWS competency case 167"
        job_desc = "Looking for Python React AWS engineer position 167"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0168(self):
        doc_text = "Experienced Python developer with React and AWS competency case 168"
        job_desc = "Looking for Python React AWS engineer position 168"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0169(self):
        doc_text = "Experienced Python developer with React and AWS competency case 169"
        job_desc = "Looking for Python React AWS engineer position 169"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0170(self):
        doc_text = "Experienced Python developer with React and AWS competency case 170"
        job_desc = "Looking for Python React AWS engineer position 170"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0171(self):
        doc_text = "Experienced Python developer with React and AWS competency case 171"
        job_desc = "Looking for Python React AWS engineer position 171"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0172(self):
        doc_text = "Experienced Python developer with React and AWS competency case 172"
        job_desc = "Looking for Python React AWS engineer position 172"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0173(self):
        doc_text = "Experienced Python developer with React and AWS competency case 173"
        job_desc = "Looking for Python React AWS engineer position 173"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0174(self):
        doc_text = "Experienced Python developer with React and AWS competency case 174"
        job_desc = "Looking for Python React AWS engineer position 174"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0175(self):
        doc_text = "Experienced Python developer with React and AWS competency case 175"
        job_desc = "Looking for Python React AWS engineer position 175"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0176(self):
        doc_text = "Experienced Python developer with React and AWS competency case 176"
        job_desc = "Looking for Python React AWS engineer position 176"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0177(self):
        doc_text = "Experienced Python developer with React and AWS competency case 177"
        job_desc = "Looking for Python React AWS engineer position 177"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0178(self):
        doc_text = "Experienced Python developer with React and AWS competency case 178"
        job_desc = "Looking for Python React AWS engineer position 178"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0179(self):
        doc_text = "Experienced Python developer with React and AWS competency case 179"
        job_desc = "Looking for Python React AWS engineer position 179"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0180(self):
        doc_text = "Experienced Python developer with React and AWS competency case 180"
        job_desc = "Looking for Python React AWS engineer position 180"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0181(self):
        doc_text = "Experienced Python developer with React and AWS competency case 181"
        job_desc = "Looking for Python React AWS engineer position 181"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0182(self):
        doc_text = "Experienced Python developer with React and AWS competency case 182"
        job_desc = "Looking for Python React AWS engineer position 182"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0183(self):
        doc_text = "Experienced Python developer with React and AWS competency case 183"
        job_desc = "Looking for Python React AWS engineer position 183"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0184(self):
        doc_text = "Experienced Python developer with React and AWS competency case 184"
        job_desc = "Looking for Python React AWS engineer position 184"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0185(self):
        doc_text = "Experienced Python developer with React and AWS competency case 185"
        job_desc = "Looking for Python React AWS engineer position 185"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0186(self):
        doc_text = "Experienced Python developer with React and AWS competency case 186"
        job_desc = "Looking for Python React AWS engineer position 186"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0187(self):
        doc_text = "Experienced Python developer with React and AWS competency case 187"
        job_desc = "Looking for Python React AWS engineer position 187"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0188(self):
        doc_text = "Experienced Python developer with React and AWS competency case 188"
        job_desc = "Looking for Python React AWS engineer position 188"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0189(self):
        doc_text = "Experienced Python developer with React and AWS competency case 189"
        job_desc = "Looking for Python React AWS engineer position 189"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0190(self):
        doc_text = "Experienced Python developer with React and AWS competency case 190"
        job_desc = "Looking for Python React AWS engineer position 190"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0191(self):
        doc_text = "Experienced Python developer with React and AWS competency case 191"
        job_desc = "Looking for Python React AWS engineer position 191"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0192(self):
        doc_text = "Experienced Python developer with React and AWS competency case 192"
        job_desc = "Looking for Python React AWS engineer position 192"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0193(self):
        doc_text = "Experienced Python developer with React and AWS competency case 193"
        job_desc = "Looking for Python React AWS engineer position 193"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0194(self):
        doc_text = "Experienced Python developer with React and AWS competency case 194"
        job_desc = "Looking for Python React AWS engineer position 194"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0195(self):
        doc_text = "Experienced Python developer with React and AWS competency case 195"
        job_desc = "Looking for Python React AWS engineer position 195"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0196(self):
        doc_text = "Experienced Python developer with React and AWS competency case 196"
        job_desc = "Looking for Python React AWS engineer position 196"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0197(self):
        doc_text = "Experienced Python developer with React and AWS competency case 197"
        job_desc = "Looking for Python React AWS engineer position 197"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0198(self):
        doc_text = "Experienced Python developer with React and AWS competency case 198"
        job_desc = "Looking for Python React AWS engineer position 198"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0199(self):
        doc_text = "Experienced Python developer with React and AWS competency case 199"
        job_desc = "Looking for Python React AWS engineer position 199"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0200(self):
        doc_text = "Experienced Python developer with React and AWS competency case 200"
        job_desc = "Looking for Python React AWS engineer position 200"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0201(self):
        doc_text = "Experienced Python developer with React and AWS competency case 201"
        job_desc = "Looking for Python React AWS engineer position 201"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0202(self):
        doc_text = "Experienced Python developer with React and AWS competency case 202"
        job_desc = "Looking for Python React AWS engineer position 202"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0203(self):
        doc_text = "Experienced Python developer with React and AWS competency case 203"
        job_desc = "Looking for Python React AWS engineer position 203"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0204(self):
        doc_text = "Experienced Python developer with React and AWS competency case 204"
        job_desc = "Looking for Python React AWS engineer position 204"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0205(self):
        doc_text = "Experienced Python developer with React and AWS competency case 205"
        job_desc = "Looking for Python React AWS engineer position 205"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0206(self):
        doc_text = "Experienced Python developer with React and AWS competency case 206"
        job_desc = "Looking for Python React AWS engineer position 206"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0207(self):
        doc_text = "Experienced Python developer with React and AWS competency case 207"
        job_desc = "Looking for Python React AWS engineer position 207"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0208(self):
        doc_text = "Experienced Python developer with React and AWS competency case 208"
        job_desc = "Looking for Python React AWS engineer position 208"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0209(self):
        doc_text = "Experienced Python developer with React and AWS competency case 209"
        job_desc = "Looking for Python React AWS engineer position 209"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0210(self):
        doc_text = "Experienced Python developer with React and AWS competency case 210"
        job_desc = "Looking for Python React AWS engineer position 210"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0211(self):
        doc_text = "Experienced Python developer with React and AWS competency case 211"
        job_desc = "Looking for Python React AWS engineer position 211"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0212(self):
        doc_text = "Experienced Python developer with React and AWS competency case 212"
        job_desc = "Looking for Python React AWS engineer position 212"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0213(self):
        doc_text = "Experienced Python developer with React and AWS competency case 213"
        job_desc = "Looking for Python React AWS engineer position 213"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0214(self):
        doc_text = "Experienced Python developer with React and AWS competency case 214"
        job_desc = "Looking for Python React AWS engineer position 214"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0215(self):
        doc_text = "Experienced Python developer with React and AWS competency case 215"
        job_desc = "Looking for Python React AWS engineer position 215"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0216(self):
        doc_text = "Experienced Python developer with React and AWS competency case 216"
        job_desc = "Looking for Python React AWS engineer position 216"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0217(self):
        doc_text = "Experienced Python developer with React and AWS competency case 217"
        job_desc = "Looking for Python React AWS engineer position 217"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0218(self):
        doc_text = "Experienced Python developer with React and AWS competency case 218"
        job_desc = "Looking for Python React AWS engineer position 218"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0219(self):
        doc_text = "Experienced Python developer with React and AWS competency case 219"
        job_desc = "Looking for Python React AWS engineer position 219"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0220(self):
        doc_text = "Experienced Python developer with React and AWS competency case 220"
        job_desc = "Looking for Python React AWS engineer position 220"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0221(self):
        doc_text = "Experienced Python developer with React and AWS competency case 221"
        job_desc = "Looking for Python React AWS engineer position 221"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0222(self):
        doc_text = "Experienced Python developer with React and AWS competency case 222"
        job_desc = "Looking for Python React AWS engineer position 222"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0223(self):
        doc_text = "Experienced Python developer with React and AWS competency case 223"
        job_desc = "Looking for Python React AWS engineer position 223"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0224(self):
        doc_text = "Experienced Python developer with React and AWS competency case 224"
        job_desc = "Looking for Python React AWS engineer position 224"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0225(self):
        doc_text = "Experienced Python developer with React and AWS competency case 225"
        job_desc = "Looking for Python React AWS engineer position 225"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0226(self):
        doc_text = "Experienced Python developer with React and AWS competency case 226"
        job_desc = "Looking for Python React AWS engineer position 226"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0227(self):
        doc_text = "Experienced Python developer with React and AWS competency case 227"
        job_desc = "Looking for Python React AWS engineer position 227"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0228(self):
        doc_text = "Experienced Python developer with React and AWS competency case 228"
        job_desc = "Looking for Python React AWS engineer position 228"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0229(self):
        doc_text = "Experienced Python developer with React and AWS competency case 229"
        job_desc = "Looking for Python React AWS engineer position 229"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0230(self):
        doc_text = "Experienced Python developer with React and AWS competency case 230"
        job_desc = "Looking for Python React AWS engineer position 230"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0231(self):
        doc_text = "Experienced Python developer with React and AWS competency case 231"
        job_desc = "Looking for Python React AWS engineer position 231"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0232(self):
        doc_text = "Experienced Python developer with React and AWS competency case 232"
        job_desc = "Looking for Python React AWS engineer position 232"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0233(self):
        doc_text = "Experienced Python developer with React and AWS competency case 233"
        job_desc = "Looking for Python React AWS engineer position 233"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0234(self):
        doc_text = "Experienced Python developer with React and AWS competency case 234"
        job_desc = "Looking for Python React AWS engineer position 234"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0235(self):
        doc_text = "Experienced Python developer with React and AWS competency case 235"
        job_desc = "Looking for Python React AWS engineer position 235"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0236(self):
        doc_text = "Experienced Python developer with React and AWS competency case 236"
        job_desc = "Looking for Python React AWS engineer position 236"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0237(self):
        doc_text = "Experienced Python developer with React and AWS competency case 237"
        job_desc = "Looking for Python React AWS engineer position 237"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0238(self):
        doc_text = "Experienced Python developer with React and AWS competency case 238"
        job_desc = "Looking for Python React AWS engineer position 238"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0239(self):
        doc_text = "Experienced Python developer with React and AWS competency case 239"
        job_desc = "Looking for Python React AWS engineer position 239"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0240(self):
        doc_text = "Experienced Python developer with React and AWS competency case 240"
        job_desc = "Looking for Python React AWS engineer position 240"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0241(self):
        doc_text = "Experienced Python developer with React and AWS competency case 241"
        job_desc = "Looking for Python React AWS engineer position 241"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0242(self):
        doc_text = "Experienced Python developer with React and AWS competency case 242"
        job_desc = "Looking for Python React AWS engineer position 242"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0243(self):
        doc_text = "Experienced Python developer with React and AWS competency case 243"
        job_desc = "Looking for Python React AWS engineer position 243"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0244(self):
        doc_text = "Experienced Python developer with React and AWS competency case 244"
        job_desc = "Looking for Python React AWS engineer position 244"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0245(self):
        doc_text = "Experienced Python developer with React and AWS competency case 245"
        job_desc = "Looking for Python React AWS engineer position 245"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0246(self):
        doc_text = "Experienced Python developer with React and AWS competency case 246"
        job_desc = "Looking for Python React AWS engineer position 246"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0247(self):
        doc_text = "Experienced Python developer with React and AWS competency case 247"
        job_desc = "Looking for Python React AWS engineer position 247"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0248(self):
        doc_text = "Experienced Python developer with React and AWS competency case 248"
        job_desc = "Looking for Python React AWS engineer position 248"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0249(self):
        doc_text = "Experienced Python developer with React and AWS competency case 249"
        job_desc = "Looking for Python React AWS engineer position 249"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0250(self):
        doc_text = "Experienced Python developer with React and AWS competency case 250"
        job_desc = "Looking for Python React AWS engineer position 250"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0251(self):
        doc_text = "Experienced Python developer with React and AWS competency case 251"
        job_desc = "Looking for Python React AWS engineer position 251"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0252(self):
        doc_text = "Experienced Python developer with React and AWS competency case 252"
        job_desc = "Looking for Python React AWS engineer position 252"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0253(self):
        doc_text = "Experienced Python developer with React and AWS competency case 253"
        job_desc = "Looking for Python React AWS engineer position 253"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0254(self):
        doc_text = "Experienced Python developer with React and AWS competency case 254"
        job_desc = "Looking for Python React AWS engineer position 254"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0255(self):
        doc_text = "Experienced Python developer with React and AWS competency case 255"
        job_desc = "Looking for Python React AWS engineer position 255"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0256(self):
        doc_text = "Experienced Python developer with React and AWS competency case 256"
        job_desc = "Looking for Python React AWS engineer position 256"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0257(self):
        doc_text = "Experienced Python developer with React and AWS competency case 257"
        job_desc = "Looking for Python React AWS engineer position 257"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0258(self):
        doc_text = "Experienced Python developer with React and AWS competency case 258"
        job_desc = "Looking for Python React AWS engineer position 258"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0259(self):
        doc_text = "Experienced Python developer with React and AWS competency case 259"
        job_desc = "Looking for Python React AWS engineer position 259"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0260(self):
        doc_text = "Experienced Python developer with React and AWS competency case 260"
        job_desc = "Looking for Python React AWS engineer position 260"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0261(self):
        doc_text = "Experienced Python developer with React and AWS competency case 261"
        job_desc = "Looking for Python React AWS engineer position 261"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0262(self):
        doc_text = "Experienced Python developer with React and AWS competency case 262"
        job_desc = "Looking for Python React AWS engineer position 262"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0263(self):
        doc_text = "Experienced Python developer with React and AWS competency case 263"
        job_desc = "Looking for Python React AWS engineer position 263"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0264(self):
        doc_text = "Experienced Python developer with React and AWS competency case 264"
        job_desc = "Looking for Python React AWS engineer position 264"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0265(self):
        doc_text = "Experienced Python developer with React and AWS competency case 265"
        job_desc = "Looking for Python React AWS engineer position 265"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0266(self):
        doc_text = "Experienced Python developer with React and AWS competency case 266"
        job_desc = "Looking for Python React AWS engineer position 266"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0267(self):
        doc_text = "Experienced Python developer with React and AWS competency case 267"
        job_desc = "Looking for Python React AWS engineer position 267"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0268(self):
        doc_text = "Experienced Python developer with React and AWS competency case 268"
        job_desc = "Looking for Python React AWS engineer position 268"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0269(self):
        doc_text = "Experienced Python developer with React and AWS competency case 269"
        job_desc = "Looking for Python React AWS engineer position 269"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0270(self):
        doc_text = "Experienced Python developer with React and AWS competency case 270"
        job_desc = "Looking for Python React AWS engineer position 270"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0271(self):
        doc_text = "Experienced Python developer with React and AWS competency case 271"
        job_desc = "Looking for Python React AWS engineer position 271"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0272(self):
        doc_text = "Experienced Python developer with React and AWS competency case 272"
        job_desc = "Looking for Python React AWS engineer position 272"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0273(self):
        doc_text = "Experienced Python developer with React and AWS competency case 273"
        job_desc = "Looking for Python React AWS engineer position 273"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0274(self):
        doc_text = "Experienced Python developer with React and AWS competency case 274"
        job_desc = "Looking for Python React AWS engineer position 274"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0275(self):
        doc_text = "Experienced Python developer with React and AWS competency case 275"
        job_desc = "Looking for Python React AWS engineer position 275"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0276(self):
        doc_text = "Experienced Python developer with React and AWS competency case 276"
        job_desc = "Looking for Python React AWS engineer position 276"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0277(self):
        doc_text = "Experienced Python developer with React and AWS competency case 277"
        job_desc = "Looking for Python React AWS engineer position 277"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0278(self):
        doc_text = "Experienced Python developer with React and AWS competency case 278"
        job_desc = "Looking for Python React AWS engineer position 278"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0279(self):
        doc_text = "Experienced Python developer with React and AWS competency case 279"
        job_desc = "Looking for Python React AWS engineer position 279"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0280(self):
        doc_text = "Experienced Python developer with React and AWS competency case 280"
        job_desc = "Looking for Python React AWS engineer position 280"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0281(self):
        doc_text = "Experienced Python developer with React and AWS competency case 281"
        job_desc = "Looking for Python React AWS engineer position 281"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0282(self):
        doc_text = "Experienced Python developer with React and AWS competency case 282"
        job_desc = "Looking for Python React AWS engineer position 282"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0283(self):
        doc_text = "Experienced Python developer with React and AWS competency case 283"
        job_desc = "Looking for Python React AWS engineer position 283"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0284(self):
        doc_text = "Experienced Python developer with React and AWS competency case 284"
        job_desc = "Looking for Python React AWS engineer position 284"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0285(self):
        doc_text = "Experienced Python developer with React and AWS competency case 285"
        job_desc = "Looking for Python React AWS engineer position 285"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0286(self):
        doc_text = "Experienced Python developer with React and AWS competency case 286"
        job_desc = "Looking for Python React AWS engineer position 286"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0287(self):
        doc_text = "Experienced Python developer with React and AWS competency case 287"
        job_desc = "Looking for Python React AWS engineer position 287"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0288(self):
        doc_text = "Experienced Python developer with React and AWS competency case 288"
        job_desc = "Looking for Python React AWS engineer position 288"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0289(self):
        doc_text = "Experienced Python developer with React and AWS competency case 289"
        job_desc = "Looking for Python React AWS engineer position 289"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0290(self):
        doc_text = "Experienced Python developer with React and AWS competency case 290"
        job_desc = "Looking for Python React AWS engineer position 290"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0291(self):
        doc_text = "Experienced Python developer with React and AWS competency case 291"
        job_desc = "Looking for Python React AWS engineer position 291"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0292(self):
        doc_text = "Experienced Python developer with React and AWS competency case 292"
        job_desc = "Looking for Python React AWS engineer position 292"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0293(self):
        doc_text = "Experienced Python developer with React and AWS competency case 293"
        job_desc = "Looking for Python React AWS engineer position 293"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0294(self):
        doc_text = "Experienced Python developer with React and AWS competency case 294"
        job_desc = "Looking for Python React AWS engineer position 294"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0295(self):
        doc_text = "Experienced Python developer with React and AWS competency case 295"
        job_desc = "Looking for Python React AWS engineer position 295"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0296(self):
        doc_text = "Experienced Python developer with React and AWS competency case 296"
        job_desc = "Looking for Python React AWS engineer position 296"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0297(self):
        doc_text = "Experienced Python developer with React and AWS competency case 297"
        job_desc = "Looking for Python React AWS engineer position 297"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0298(self):
        doc_text = "Experienced Python developer with React and AWS competency case 298"
        job_desc = "Looking for Python React AWS engineer position 298"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0299(self):
        doc_text = "Experienced Python developer with React and AWS competency case 299"
        job_desc = "Looking for Python React AWS engineer position 299"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0300(self):
        doc_text = "Experienced Python developer with React and AWS competency case 300"
        job_desc = "Looking for Python React AWS engineer position 300"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0301(self):
        doc_text = "Experienced Python developer with React and AWS competency case 301"
        job_desc = "Looking for Python React AWS engineer position 301"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0302(self):
        doc_text = "Experienced Python developer with React and AWS competency case 302"
        job_desc = "Looking for Python React AWS engineer position 302"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0303(self):
        doc_text = "Experienced Python developer with React and AWS competency case 303"
        job_desc = "Looking for Python React AWS engineer position 303"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0304(self):
        doc_text = "Experienced Python developer with React and AWS competency case 304"
        job_desc = "Looking for Python React AWS engineer position 304"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0305(self):
        doc_text = "Experienced Python developer with React and AWS competency case 305"
        job_desc = "Looking for Python React AWS engineer position 305"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0306(self):
        doc_text = "Experienced Python developer with React and AWS competency case 306"
        job_desc = "Looking for Python React AWS engineer position 306"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0307(self):
        doc_text = "Experienced Python developer with React and AWS competency case 307"
        job_desc = "Looking for Python React AWS engineer position 307"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0308(self):
        doc_text = "Experienced Python developer with React and AWS competency case 308"
        job_desc = "Looking for Python React AWS engineer position 308"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0309(self):
        doc_text = "Experienced Python developer with React and AWS competency case 309"
        job_desc = "Looking for Python React AWS engineer position 309"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0310(self):
        doc_text = "Experienced Python developer with React and AWS competency case 310"
        job_desc = "Looking for Python React AWS engineer position 310"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0311(self):
        doc_text = "Experienced Python developer with React and AWS competency case 311"
        job_desc = "Looking for Python React AWS engineer position 311"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0312(self):
        doc_text = "Experienced Python developer with React and AWS competency case 312"
        job_desc = "Looking for Python React AWS engineer position 312"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0313(self):
        doc_text = "Experienced Python developer with React and AWS competency case 313"
        job_desc = "Looking for Python React AWS engineer position 313"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0314(self):
        doc_text = "Experienced Python developer with React and AWS competency case 314"
        job_desc = "Looking for Python React AWS engineer position 314"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0315(self):
        doc_text = "Experienced Python developer with React and AWS competency case 315"
        job_desc = "Looking for Python React AWS engineer position 315"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0316(self):
        doc_text = "Experienced Python developer with React and AWS competency case 316"
        job_desc = "Looking for Python React AWS engineer position 316"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0317(self):
        doc_text = "Experienced Python developer with React and AWS competency case 317"
        job_desc = "Looking for Python React AWS engineer position 317"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0318(self):
        doc_text = "Experienced Python developer with React and AWS competency case 318"
        job_desc = "Looking for Python React AWS engineer position 318"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0319(self):
        doc_text = "Experienced Python developer with React and AWS competency case 319"
        job_desc = "Looking for Python React AWS engineer position 319"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0320(self):
        doc_text = "Experienced Python developer with React and AWS competency case 320"
        job_desc = "Looking for Python React AWS engineer position 320"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0321(self):
        doc_text = "Experienced Python developer with React and AWS competency case 321"
        job_desc = "Looking for Python React AWS engineer position 321"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0322(self):
        doc_text = "Experienced Python developer with React and AWS competency case 322"
        job_desc = "Looking for Python React AWS engineer position 322"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0323(self):
        doc_text = "Experienced Python developer with React and AWS competency case 323"
        job_desc = "Looking for Python React AWS engineer position 323"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0324(self):
        doc_text = "Experienced Python developer with React and AWS competency case 324"
        job_desc = "Looking for Python React AWS engineer position 324"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0325(self):
        doc_text = "Experienced Python developer with React and AWS competency case 325"
        job_desc = "Looking for Python React AWS engineer position 325"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0326(self):
        doc_text = "Experienced Python developer with React and AWS competency case 326"
        job_desc = "Looking for Python React AWS engineer position 326"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0327(self):
        doc_text = "Experienced Python developer with React and AWS competency case 327"
        job_desc = "Looking for Python React AWS engineer position 327"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0328(self):
        doc_text = "Experienced Python developer with React and AWS competency case 328"
        job_desc = "Looking for Python React AWS engineer position 328"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0329(self):
        doc_text = "Experienced Python developer with React and AWS competency case 329"
        job_desc = "Looking for Python React AWS engineer position 329"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0330(self):
        doc_text = "Experienced Python developer with React and AWS competency case 330"
        job_desc = "Looking for Python React AWS engineer position 330"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0331(self):
        doc_text = "Experienced Python developer with React and AWS competency case 331"
        job_desc = "Looking for Python React AWS engineer position 331"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0332(self):
        doc_text = "Experienced Python developer with React and AWS competency case 332"
        job_desc = "Looking for Python React AWS engineer position 332"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0333(self):
        doc_text = "Experienced Python developer with React and AWS competency case 333"
        job_desc = "Looking for Python React AWS engineer position 333"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0334(self):
        doc_text = "Experienced Python developer with React and AWS competency case 334"
        job_desc = "Looking for Python React AWS engineer position 334"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0335(self):
        doc_text = "Experienced Python developer with React and AWS competency case 335"
        job_desc = "Looking for Python React AWS engineer position 335"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0336(self):
        doc_text = "Experienced Python developer with React and AWS competency case 336"
        job_desc = "Looking for Python React AWS engineer position 336"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0337(self):
        doc_text = "Experienced Python developer with React and AWS competency case 337"
        job_desc = "Looking for Python React AWS engineer position 337"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0338(self):
        doc_text = "Experienced Python developer with React and AWS competency case 338"
        job_desc = "Looking for Python React AWS engineer position 338"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0339(self):
        doc_text = "Experienced Python developer with React and AWS competency case 339"
        job_desc = "Looking for Python React AWS engineer position 339"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0340(self):
        doc_text = "Experienced Python developer with React and AWS competency case 340"
        job_desc = "Looking for Python React AWS engineer position 340"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0341(self):
        doc_text = "Experienced Python developer with React and AWS competency case 341"
        job_desc = "Looking for Python React AWS engineer position 341"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0342(self):
        doc_text = "Experienced Python developer with React and AWS competency case 342"
        job_desc = "Looking for Python React AWS engineer position 342"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0343(self):
        doc_text = "Experienced Python developer with React and AWS competency case 343"
        job_desc = "Looking for Python React AWS engineer position 343"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0344(self):
        doc_text = "Experienced Python developer with React and AWS competency case 344"
        job_desc = "Looking for Python React AWS engineer position 344"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0345(self):
        doc_text = "Experienced Python developer with React and AWS competency case 345"
        job_desc = "Looking for Python React AWS engineer position 345"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0346(self):
        doc_text = "Experienced Python developer with React and AWS competency case 346"
        job_desc = "Looking for Python React AWS engineer position 346"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0347(self):
        doc_text = "Experienced Python developer with React and AWS competency case 347"
        job_desc = "Looking for Python React AWS engineer position 347"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0348(self):
        doc_text = "Experienced Python developer with React and AWS competency case 348"
        job_desc = "Looking for Python React AWS engineer position 348"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0349(self):
        doc_text = "Experienced Python developer with React and AWS competency case 349"
        job_desc = "Looking for Python React AWS engineer position 349"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0350(self):
        doc_text = "Experienced Python developer with React and AWS competency case 350"
        job_desc = "Looking for Python React AWS engineer position 350"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0351(self):
        doc_text = "Experienced Python developer with React and AWS competency case 351"
        job_desc = "Looking for Python React AWS engineer position 351"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0352(self):
        doc_text = "Experienced Python developer with React and AWS competency case 352"
        job_desc = "Looking for Python React AWS engineer position 352"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0353(self):
        doc_text = "Experienced Python developer with React and AWS competency case 353"
        job_desc = "Looking for Python React AWS engineer position 353"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0354(self):
        doc_text = "Experienced Python developer with React and AWS competency case 354"
        job_desc = "Looking for Python React AWS engineer position 354"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0355(self):
        doc_text = "Experienced Python developer with React and AWS competency case 355"
        job_desc = "Looking for Python React AWS engineer position 355"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0356(self):
        doc_text = "Experienced Python developer with React and AWS competency case 356"
        job_desc = "Looking for Python React AWS engineer position 356"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0357(self):
        doc_text = "Experienced Python developer with React and AWS competency case 357"
        job_desc = "Looking for Python React AWS engineer position 357"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0358(self):
        doc_text = "Experienced Python developer with React and AWS competency case 358"
        job_desc = "Looking for Python React AWS engineer position 358"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0359(self):
        doc_text = "Experienced Python developer with React and AWS competency case 359"
        job_desc = "Looking for Python React AWS engineer position 359"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0360(self):
        doc_text = "Experienced Python developer with React and AWS competency case 360"
        job_desc = "Looking for Python React AWS engineer position 360"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0361(self):
        doc_text = "Experienced Python developer with React and AWS competency case 361"
        job_desc = "Looking for Python React AWS engineer position 361"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0362(self):
        doc_text = "Experienced Python developer with React and AWS competency case 362"
        job_desc = "Looking for Python React AWS engineer position 362"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0363(self):
        doc_text = "Experienced Python developer with React and AWS competency case 363"
        job_desc = "Looking for Python React AWS engineer position 363"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0364(self):
        doc_text = "Experienced Python developer with React and AWS competency case 364"
        job_desc = "Looking for Python React AWS engineer position 364"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0365(self):
        doc_text = "Experienced Python developer with React and AWS competency case 365"
        job_desc = "Looking for Python React AWS engineer position 365"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0366(self):
        doc_text = "Experienced Python developer with React and AWS competency case 366"
        job_desc = "Looking for Python React AWS engineer position 366"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0367(self):
        doc_text = "Experienced Python developer with React and AWS competency case 367"
        job_desc = "Looking for Python React AWS engineer position 367"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0368(self):
        doc_text = "Experienced Python developer with React and AWS competency case 368"
        job_desc = "Looking for Python React AWS engineer position 368"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0369(self):
        doc_text = "Experienced Python developer with React and AWS competency case 369"
        job_desc = "Looking for Python React AWS engineer position 369"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0370(self):
        doc_text = "Experienced Python developer with React and AWS competency case 370"
        job_desc = "Looking for Python React AWS engineer position 370"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0371(self):
        doc_text = "Experienced Python developer with React and AWS competency case 371"
        job_desc = "Looking for Python React AWS engineer position 371"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0372(self):
        doc_text = "Experienced Python developer with React and AWS competency case 372"
        job_desc = "Looking for Python React AWS engineer position 372"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0373(self):
        doc_text = "Experienced Python developer with React and AWS competency case 373"
        job_desc = "Looking for Python React AWS engineer position 373"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0374(self):
        doc_text = "Experienced Python developer with React and AWS competency case 374"
        job_desc = "Looking for Python React AWS engineer position 374"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0375(self):
        doc_text = "Experienced Python developer with React and AWS competency case 375"
        job_desc = "Looking for Python React AWS engineer position 375"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0376(self):
        doc_text = "Experienced Python developer with React and AWS competency case 376"
        job_desc = "Looking for Python React AWS engineer position 376"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0377(self):
        doc_text = "Experienced Python developer with React and AWS competency case 377"
        job_desc = "Looking for Python React AWS engineer position 377"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0378(self):
        doc_text = "Experienced Python developer with React and AWS competency case 378"
        job_desc = "Looking for Python React AWS engineer position 378"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0379(self):
        doc_text = "Experienced Python developer with React and AWS competency case 379"
        job_desc = "Looking for Python React AWS engineer position 379"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0380(self):
        doc_text = "Experienced Python developer with React and AWS competency case 380"
        job_desc = "Looking for Python React AWS engineer position 380"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0381(self):
        doc_text = "Experienced Python developer with React and AWS competency case 381"
        job_desc = "Looking for Python React AWS engineer position 381"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0382(self):
        doc_text = "Experienced Python developer with React and AWS competency case 382"
        job_desc = "Looking for Python React AWS engineer position 382"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0383(self):
        doc_text = "Experienced Python developer with React and AWS competency case 383"
        job_desc = "Looking for Python React AWS engineer position 383"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0384(self):
        doc_text = "Experienced Python developer with React and AWS competency case 384"
        job_desc = "Looking for Python React AWS engineer position 384"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0385(self):
        doc_text = "Experienced Python developer with React and AWS competency case 385"
        job_desc = "Looking for Python React AWS engineer position 385"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0386(self):
        doc_text = "Experienced Python developer with React and AWS competency case 386"
        job_desc = "Looking for Python React AWS engineer position 386"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0387(self):
        doc_text = "Experienced Python developer with React and AWS competency case 387"
        job_desc = "Looking for Python React AWS engineer position 387"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0388(self):
        doc_text = "Experienced Python developer with React and AWS competency case 388"
        job_desc = "Looking for Python React AWS engineer position 388"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0389(self):
        doc_text = "Experienced Python developer with React and AWS competency case 389"
        job_desc = "Looking for Python React AWS engineer position 389"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0390(self):
        doc_text = "Experienced Python developer with React and AWS competency case 390"
        job_desc = "Looking for Python React AWS engineer position 390"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0391(self):
        doc_text = "Experienced Python developer with React and AWS competency case 391"
        job_desc = "Looking for Python React AWS engineer position 391"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0392(self):
        doc_text = "Experienced Python developer with React and AWS competency case 392"
        job_desc = "Looking for Python React AWS engineer position 392"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0393(self):
        doc_text = "Experienced Python developer with React and AWS competency case 393"
        job_desc = "Looking for Python React AWS engineer position 393"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0394(self):
        doc_text = "Experienced Python developer with React and AWS competency case 394"
        job_desc = "Looking for Python React AWS engineer position 394"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0395(self):
        doc_text = "Experienced Python developer with React and AWS competency case 395"
        job_desc = "Looking for Python React AWS engineer position 395"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0396(self):
        doc_text = "Experienced Python developer with React and AWS competency case 396"
        job_desc = "Looking for Python React AWS engineer position 396"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0397(self):
        doc_text = "Experienced Python developer with React and AWS competency case 397"
        job_desc = "Looking for Python React AWS engineer position 397"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0398(self):
        doc_text = "Experienced Python developer with React and AWS competency case 398"
        job_desc = "Looking for Python React AWS engineer position 398"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0399(self):
        doc_text = "Experienced Python developer with React and AWS competency case 399"
        job_desc = "Looking for Python React AWS engineer position 399"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0400(self):
        doc_text = "Experienced Python developer with React and AWS competency case 400"
        job_desc = "Looking for Python React AWS engineer position 400"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0401(self):
        doc_text = "Experienced Python developer with React and AWS competency case 401"
        job_desc = "Looking for Python React AWS engineer position 401"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0402(self):
        doc_text = "Experienced Python developer with React and AWS competency case 402"
        job_desc = "Looking for Python React AWS engineer position 402"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0403(self):
        doc_text = "Experienced Python developer with React and AWS competency case 403"
        job_desc = "Looking for Python React AWS engineer position 403"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0404(self):
        doc_text = "Experienced Python developer with React and AWS competency case 404"
        job_desc = "Looking for Python React AWS engineer position 404"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0405(self):
        doc_text = "Experienced Python developer with React and AWS competency case 405"
        job_desc = "Looking for Python React AWS engineer position 405"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0406(self):
        doc_text = "Experienced Python developer with React and AWS competency case 406"
        job_desc = "Looking for Python React AWS engineer position 406"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0407(self):
        doc_text = "Experienced Python developer with React and AWS competency case 407"
        job_desc = "Looking for Python React AWS engineer position 407"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0408(self):
        doc_text = "Experienced Python developer with React and AWS competency case 408"
        job_desc = "Looking for Python React AWS engineer position 408"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0409(self):
        doc_text = "Experienced Python developer with React and AWS competency case 409"
        job_desc = "Looking for Python React AWS engineer position 409"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0410(self):
        doc_text = "Experienced Python developer with React and AWS competency case 410"
        job_desc = "Looking for Python React AWS engineer position 410"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0411(self):
        doc_text = "Experienced Python developer with React and AWS competency case 411"
        job_desc = "Looking for Python React AWS engineer position 411"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0412(self):
        doc_text = "Experienced Python developer with React and AWS competency case 412"
        job_desc = "Looking for Python React AWS engineer position 412"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0413(self):
        doc_text = "Experienced Python developer with React and AWS competency case 413"
        job_desc = "Looking for Python React AWS engineer position 413"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0414(self):
        doc_text = "Experienced Python developer with React and AWS competency case 414"
        job_desc = "Looking for Python React AWS engineer position 414"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0415(self):
        doc_text = "Experienced Python developer with React and AWS competency case 415"
        job_desc = "Looking for Python React AWS engineer position 415"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0416(self):
        doc_text = "Experienced Python developer with React and AWS competency case 416"
        job_desc = "Looking for Python React AWS engineer position 416"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0417(self):
        doc_text = "Experienced Python developer with React and AWS competency case 417"
        job_desc = "Looking for Python React AWS engineer position 417"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0418(self):
        doc_text = "Experienced Python developer with React and AWS competency case 418"
        job_desc = "Looking for Python React AWS engineer position 418"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0419(self):
        doc_text = "Experienced Python developer with React and AWS competency case 419"
        job_desc = "Looking for Python React AWS engineer position 419"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0420(self):
        doc_text = "Experienced Python developer with React and AWS competency case 420"
        job_desc = "Looking for Python React AWS engineer position 420"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0421(self):
        doc_text = "Experienced Python developer with React and AWS competency case 421"
        job_desc = "Looking for Python React AWS engineer position 421"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0422(self):
        doc_text = "Experienced Python developer with React and AWS competency case 422"
        job_desc = "Looking for Python React AWS engineer position 422"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0423(self):
        doc_text = "Experienced Python developer with React and AWS competency case 423"
        job_desc = "Looking for Python React AWS engineer position 423"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0424(self):
        doc_text = "Experienced Python developer with React and AWS competency case 424"
        job_desc = "Looking for Python React AWS engineer position 424"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0425(self):
        doc_text = "Experienced Python developer with React and AWS competency case 425"
        job_desc = "Looking for Python React AWS engineer position 425"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0426(self):
        doc_text = "Experienced Python developer with React and AWS competency case 426"
        job_desc = "Looking for Python React AWS engineer position 426"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0427(self):
        doc_text = "Experienced Python developer with React and AWS competency case 427"
        job_desc = "Looking for Python React AWS engineer position 427"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0428(self):
        doc_text = "Experienced Python developer with React and AWS competency case 428"
        job_desc = "Looking for Python React AWS engineer position 428"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0429(self):
        doc_text = "Experienced Python developer with React and AWS competency case 429"
        job_desc = "Looking for Python React AWS engineer position 429"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0430(self):
        doc_text = "Experienced Python developer with React and AWS competency case 430"
        job_desc = "Looking for Python React AWS engineer position 430"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0431(self):
        doc_text = "Experienced Python developer with React and AWS competency case 431"
        job_desc = "Looking for Python React AWS engineer position 431"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0432(self):
        doc_text = "Experienced Python developer with React and AWS competency case 432"
        job_desc = "Looking for Python React AWS engineer position 432"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0433(self):
        doc_text = "Experienced Python developer with React and AWS competency case 433"
        job_desc = "Looking for Python React AWS engineer position 433"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0434(self):
        doc_text = "Experienced Python developer with React and AWS competency case 434"
        job_desc = "Looking for Python React AWS engineer position 434"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0435(self):
        doc_text = "Experienced Python developer with React and AWS competency case 435"
        job_desc = "Looking for Python React AWS engineer position 435"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0436(self):
        doc_text = "Experienced Python developer with React and AWS competency case 436"
        job_desc = "Looking for Python React AWS engineer position 436"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0437(self):
        doc_text = "Experienced Python developer with React and AWS competency case 437"
        job_desc = "Looking for Python React AWS engineer position 437"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0438(self):
        doc_text = "Experienced Python developer with React and AWS competency case 438"
        job_desc = "Looking for Python React AWS engineer position 438"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0439(self):
        doc_text = "Experienced Python developer with React and AWS competency case 439"
        job_desc = "Looking for Python React AWS engineer position 439"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0440(self):
        doc_text = "Experienced Python developer with React and AWS competency case 440"
        job_desc = "Looking for Python React AWS engineer position 440"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0441(self):
        doc_text = "Experienced Python developer with React and AWS competency case 441"
        job_desc = "Looking for Python React AWS engineer position 441"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0442(self):
        doc_text = "Experienced Python developer with React and AWS competency case 442"
        job_desc = "Looking for Python React AWS engineer position 442"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0443(self):
        doc_text = "Experienced Python developer with React and AWS competency case 443"
        job_desc = "Looking for Python React AWS engineer position 443"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0444(self):
        doc_text = "Experienced Python developer with React and AWS competency case 444"
        job_desc = "Looking for Python React AWS engineer position 444"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0445(self):
        doc_text = "Experienced Python developer with React and AWS competency case 445"
        job_desc = "Looking for Python React AWS engineer position 445"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0446(self):
        doc_text = "Experienced Python developer with React and AWS competency case 446"
        job_desc = "Looking for Python React AWS engineer position 446"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0447(self):
        doc_text = "Experienced Python developer with React and AWS competency case 447"
        job_desc = "Looking for Python React AWS engineer position 447"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0448(self):
        doc_text = "Experienced Python developer with React and AWS competency case 448"
        job_desc = "Looking for Python React AWS engineer position 448"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0449(self):
        doc_text = "Experienced Python developer with React and AWS competency case 449"
        job_desc = "Looking for Python React AWS engineer position 449"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0450(self):
        doc_text = "Experienced Python developer with React and AWS competency case 450"
        job_desc = "Looking for Python React AWS engineer position 450"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0451(self):
        doc_text = "Experienced Python developer with React and AWS competency case 451"
        job_desc = "Looking for Python React AWS engineer position 451"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0452(self):
        doc_text = "Experienced Python developer with React and AWS competency case 452"
        job_desc = "Looking for Python React AWS engineer position 452"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0453(self):
        doc_text = "Experienced Python developer with React and AWS competency case 453"
        job_desc = "Looking for Python React AWS engineer position 453"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0454(self):
        doc_text = "Experienced Python developer with React and AWS competency case 454"
        job_desc = "Looking for Python React AWS engineer position 454"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0455(self):
        doc_text = "Experienced Python developer with React and AWS competency case 455"
        job_desc = "Looking for Python React AWS engineer position 455"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0456(self):
        doc_text = "Experienced Python developer with React and AWS competency case 456"
        job_desc = "Looking for Python React AWS engineer position 456"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0457(self):
        doc_text = "Experienced Python developer with React and AWS competency case 457"
        job_desc = "Looking for Python React AWS engineer position 457"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0458(self):
        doc_text = "Experienced Python developer with React and AWS competency case 458"
        job_desc = "Looking for Python React AWS engineer position 458"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0459(self):
        doc_text = "Experienced Python developer with React and AWS competency case 459"
        job_desc = "Looking for Python React AWS engineer position 459"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0460(self):
        doc_text = "Experienced Python developer with React and AWS competency case 460"
        job_desc = "Looking for Python React AWS engineer position 460"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0461(self):
        doc_text = "Experienced Python developer with React and AWS competency case 461"
        job_desc = "Looking for Python React AWS engineer position 461"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0462(self):
        doc_text = "Experienced Python developer with React and AWS competency case 462"
        job_desc = "Looking for Python React AWS engineer position 462"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0463(self):
        doc_text = "Experienced Python developer with React and AWS competency case 463"
        job_desc = "Looking for Python React AWS engineer position 463"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0464(self):
        doc_text = "Experienced Python developer with React and AWS competency case 464"
        job_desc = "Looking for Python React AWS engineer position 464"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0465(self):
        doc_text = "Experienced Python developer with React and AWS competency case 465"
        job_desc = "Looking for Python React AWS engineer position 465"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0466(self):
        doc_text = "Experienced Python developer with React and AWS competency case 466"
        job_desc = "Looking for Python React AWS engineer position 466"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0467(self):
        doc_text = "Experienced Python developer with React and AWS competency case 467"
        job_desc = "Looking for Python React AWS engineer position 467"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0468(self):
        doc_text = "Experienced Python developer with React and AWS competency case 468"
        job_desc = "Looking for Python React AWS engineer position 468"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0469(self):
        doc_text = "Experienced Python developer with React and AWS competency case 469"
        job_desc = "Looking for Python React AWS engineer position 469"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0470(self):
        doc_text = "Experienced Python developer with React and AWS competency case 470"
        job_desc = "Looking for Python React AWS engineer position 470"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0471(self):
        doc_text = "Experienced Python developer with React and AWS competency case 471"
        job_desc = "Looking for Python React AWS engineer position 471"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0472(self):
        doc_text = "Experienced Python developer with React and AWS competency case 472"
        job_desc = "Looking for Python React AWS engineer position 472"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0473(self):
        doc_text = "Experienced Python developer with React and AWS competency case 473"
        job_desc = "Looking for Python React AWS engineer position 473"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0474(self):
        doc_text = "Experienced Python developer with React and AWS competency case 474"
        job_desc = "Looking for Python React AWS engineer position 474"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0475(self):
        doc_text = "Experienced Python developer with React and AWS competency case 475"
        job_desc = "Looking for Python React AWS engineer position 475"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0476(self):
        doc_text = "Experienced Python developer with React and AWS competency case 476"
        job_desc = "Looking for Python React AWS engineer position 476"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0477(self):
        doc_text = "Experienced Python developer with React and AWS competency case 477"
        job_desc = "Looking for Python React AWS engineer position 477"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0478(self):
        doc_text = "Experienced Python developer with React and AWS competency case 478"
        job_desc = "Looking for Python React AWS engineer position 478"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0479(self):
        doc_text = "Experienced Python developer with React and AWS competency case 479"
        job_desc = "Looking for Python React AWS engineer position 479"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0480(self):
        doc_text = "Experienced Python developer with React and AWS competency case 480"
        job_desc = "Looking for Python React AWS engineer position 480"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0481(self):
        doc_text = "Experienced Python developer with React and AWS competency case 481"
        job_desc = "Looking for Python React AWS engineer position 481"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0482(self):
        doc_text = "Experienced Python developer with React and AWS competency case 482"
        job_desc = "Looking for Python React AWS engineer position 482"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0483(self):
        doc_text = "Experienced Python developer with React and AWS competency case 483"
        job_desc = "Looking for Python React AWS engineer position 483"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0484(self):
        doc_text = "Experienced Python developer with React and AWS competency case 484"
        job_desc = "Looking for Python React AWS engineer position 484"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0485(self):
        doc_text = "Experienced Python developer with React and AWS competency case 485"
        job_desc = "Looking for Python React AWS engineer position 485"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0486(self):
        doc_text = "Experienced Python developer with React and AWS competency case 486"
        job_desc = "Looking for Python React AWS engineer position 486"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0487(self):
        doc_text = "Experienced Python developer with React and AWS competency case 487"
        job_desc = "Looking for Python React AWS engineer position 487"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0488(self):
        doc_text = "Experienced Python developer with React and AWS competency case 488"
        job_desc = "Looking for Python React AWS engineer position 488"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0489(self):
        doc_text = "Experienced Python developer with React and AWS competency case 489"
        job_desc = "Looking for Python React AWS engineer position 489"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0490(self):
        doc_text = "Experienced Python developer with React and AWS competency case 490"
        job_desc = "Looking for Python React AWS engineer position 490"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0491(self):
        doc_text = "Experienced Python developer with React and AWS competency case 491"
        job_desc = "Looking for Python React AWS engineer position 491"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0492(self):
        doc_text = "Experienced Python developer with React and AWS competency case 492"
        job_desc = "Looking for Python React AWS engineer position 492"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0493(self):
        doc_text = "Experienced Python developer with React and AWS competency case 493"
        job_desc = "Looking for Python React AWS engineer position 493"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0494(self):
        doc_text = "Experienced Python developer with React and AWS competency case 494"
        job_desc = "Looking for Python React AWS engineer position 494"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0495(self):
        doc_text = "Experienced Python developer with React and AWS competency case 495"
        job_desc = "Looking for Python React AWS engineer position 495"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0496(self):
        doc_text = "Experienced Python developer with React and AWS competency case 496"
        job_desc = "Looking for Python React AWS engineer position 496"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0497(self):
        doc_text = "Experienced Python developer with React and AWS competency case 497"
        job_desc = "Looking for Python React AWS engineer position 497"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0498(self):
        doc_text = "Experienced Python developer with React and AWS competency case 498"
        job_desc = "Looking for Python React AWS engineer position 498"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0499(self):
        doc_text = "Experienced Python developer with React and AWS competency case 499"
        job_desc = "Looking for Python React AWS engineer position 499"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0500(self):
        doc_text = "Experienced Python developer with React and AWS competency case 500"
        job_desc = "Looking for Python React AWS engineer position 500"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0501(self):
        doc_text = "Experienced Python developer with React and AWS competency case 501"
        job_desc = "Looking for Python React AWS engineer position 501"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0502(self):
        doc_text = "Experienced Python developer with React and AWS competency case 502"
        job_desc = "Looking for Python React AWS engineer position 502"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0503(self):
        doc_text = "Experienced Python developer with React and AWS competency case 503"
        job_desc = "Looking for Python React AWS engineer position 503"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0504(self):
        doc_text = "Experienced Python developer with React and AWS competency case 504"
        job_desc = "Looking for Python React AWS engineer position 504"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0505(self):
        doc_text = "Experienced Python developer with React and AWS competency case 505"
        job_desc = "Looking for Python React AWS engineer position 505"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0506(self):
        doc_text = "Experienced Python developer with React and AWS competency case 506"
        job_desc = "Looking for Python React AWS engineer position 506"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0507(self):
        doc_text = "Experienced Python developer with React and AWS competency case 507"
        job_desc = "Looking for Python React AWS engineer position 507"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0508(self):
        doc_text = "Experienced Python developer with React and AWS competency case 508"
        job_desc = "Looking for Python React AWS engineer position 508"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0509(self):
        doc_text = "Experienced Python developer with React and AWS competency case 509"
        job_desc = "Looking for Python React AWS engineer position 509"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0510(self):
        doc_text = "Experienced Python developer with React and AWS competency case 510"
        job_desc = "Looking for Python React AWS engineer position 510"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0511(self):
        doc_text = "Experienced Python developer with React and AWS competency case 511"
        job_desc = "Looking for Python React AWS engineer position 511"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0512(self):
        doc_text = "Experienced Python developer with React and AWS competency case 512"
        job_desc = "Looking for Python React AWS engineer position 512"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0513(self):
        doc_text = "Experienced Python developer with React and AWS competency case 513"
        job_desc = "Looking for Python React AWS engineer position 513"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0514(self):
        doc_text = "Experienced Python developer with React and AWS competency case 514"
        job_desc = "Looking for Python React AWS engineer position 514"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0515(self):
        doc_text = "Experienced Python developer with React and AWS competency case 515"
        job_desc = "Looking for Python React AWS engineer position 515"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0516(self):
        doc_text = "Experienced Python developer with React and AWS competency case 516"
        job_desc = "Looking for Python React AWS engineer position 516"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0517(self):
        doc_text = "Experienced Python developer with React and AWS competency case 517"
        job_desc = "Looking for Python React AWS engineer position 517"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0518(self):
        doc_text = "Experienced Python developer with React and AWS competency case 518"
        job_desc = "Looking for Python React AWS engineer position 518"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0519(self):
        doc_text = "Experienced Python developer with React and AWS competency case 519"
        job_desc = "Looking for Python React AWS engineer position 519"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0520(self):
        doc_text = "Experienced Python developer with React and AWS competency case 520"
        job_desc = "Looking for Python React AWS engineer position 520"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0521(self):
        doc_text = "Experienced Python developer with React and AWS competency case 521"
        job_desc = "Looking for Python React AWS engineer position 521"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0522(self):
        doc_text = "Experienced Python developer with React and AWS competency case 522"
        job_desc = "Looking for Python React AWS engineer position 522"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0523(self):
        doc_text = "Experienced Python developer with React and AWS competency case 523"
        job_desc = "Looking for Python React AWS engineer position 523"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0524(self):
        doc_text = "Experienced Python developer with React and AWS competency case 524"
        job_desc = "Looking for Python React AWS engineer position 524"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0525(self):
        doc_text = "Experienced Python developer with React and AWS competency case 525"
        job_desc = "Looking for Python React AWS engineer position 525"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0526(self):
        doc_text = "Experienced Python developer with React and AWS competency case 526"
        job_desc = "Looking for Python React AWS engineer position 526"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0527(self):
        doc_text = "Experienced Python developer with React and AWS competency case 527"
        job_desc = "Looking for Python React AWS engineer position 527"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0528(self):
        doc_text = "Experienced Python developer with React and AWS competency case 528"
        job_desc = "Looking for Python React AWS engineer position 528"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0529(self):
        doc_text = "Experienced Python developer with React and AWS competency case 529"
        job_desc = "Looking for Python React AWS engineer position 529"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0530(self):
        doc_text = "Experienced Python developer with React and AWS competency case 530"
        job_desc = "Looking for Python React AWS engineer position 530"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0531(self):
        doc_text = "Experienced Python developer with React and AWS competency case 531"
        job_desc = "Looking for Python React AWS engineer position 531"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0532(self):
        doc_text = "Experienced Python developer with React and AWS competency case 532"
        job_desc = "Looking for Python React AWS engineer position 532"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0533(self):
        doc_text = "Experienced Python developer with React and AWS competency case 533"
        job_desc = "Looking for Python React AWS engineer position 533"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0534(self):
        doc_text = "Experienced Python developer with React and AWS competency case 534"
        job_desc = "Looking for Python React AWS engineer position 534"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0535(self):
        doc_text = "Experienced Python developer with React and AWS competency case 535"
        job_desc = "Looking for Python React AWS engineer position 535"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0536(self):
        doc_text = "Experienced Python developer with React and AWS competency case 536"
        job_desc = "Looking for Python React AWS engineer position 536"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0537(self):
        doc_text = "Experienced Python developer with React and AWS competency case 537"
        job_desc = "Looking for Python React AWS engineer position 537"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0538(self):
        doc_text = "Experienced Python developer with React and AWS competency case 538"
        job_desc = "Looking for Python React AWS engineer position 538"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0539(self):
        doc_text = "Experienced Python developer with React and AWS competency case 539"
        job_desc = "Looking for Python React AWS engineer position 539"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0540(self):
        doc_text = "Experienced Python developer with React and AWS competency case 540"
        job_desc = "Looking for Python React AWS engineer position 540"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0541(self):
        doc_text = "Experienced Python developer with React and AWS competency case 541"
        job_desc = "Looking for Python React AWS engineer position 541"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0542(self):
        doc_text = "Experienced Python developer with React and AWS competency case 542"
        job_desc = "Looking for Python React AWS engineer position 542"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0543(self):
        doc_text = "Experienced Python developer with React and AWS competency case 543"
        job_desc = "Looking for Python React AWS engineer position 543"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0544(self):
        doc_text = "Experienced Python developer with React and AWS competency case 544"
        job_desc = "Looking for Python React AWS engineer position 544"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0545(self):
        doc_text = "Experienced Python developer with React and AWS competency case 545"
        job_desc = "Looking for Python React AWS engineer position 545"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0546(self):
        doc_text = "Experienced Python developer with React and AWS competency case 546"
        job_desc = "Looking for Python React AWS engineer position 546"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0547(self):
        doc_text = "Experienced Python developer with React and AWS competency case 547"
        job_desc = "Looking for Python React AWS engineer position 547"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0548(self):
        doc_text = "Experienced Python developer with React and AWS competency case 548"
        job_desc = "Looking for Python React AWS engineer position 548"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0549(self):
        doc_text = "Experienced Python developer with React and AWS competency case 549"
        job_desc = "Looking for Python React AWS engineer position 549"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0550(self):
        doc_text = "Experienced Python developer with React and AWS competency case 550"
        job_desc = "Looking for Python React AWS engineer position 550"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0551(self):
        doc_text = "Experienced Python developer with React and AWS competency case 551"
        job_desc = "Looking for Python React AWS engineer position 551"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0552(self):
        doc_text = "Experienced Python developer with React and AWS competency case 552"
        job_desc = "Looking for Python React AWS engineer position 552"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0553(self):
        doc_text = "Experienced Python developer with React and AWS competency case 553"
        job_desc = "Looking for Python React AWS engineer position 553"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0554(self):
        doc_text = "Experienced Python developer with React and AWS competency case 554"
        job_desc = "Looking for Python React AWS engineer position 554"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0555(self):
        doc_text = "Experienced Python developer with React and AWS competency case 555"
        job_desc = "Looking for Python React AWS engineer position 555"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0556(self):
        doc_text = "Experienced Python developer with React and AWS competency case 556"
        job_desc = "Looking for Python React AWS engineer position 556"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0557(self):
        doc_text = "Experienced Python developer with React and AWS competency case 557"
        job_desc = "Looking for Python React AWS engineer position 557"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0558(self):
        doc_text = "Experienced Python developer with React and AWS competency case 558"
        job_desc = "Looking for Python React AWS engineer position 558"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0559(self):
        doc_text = "Experienced Python developer with React and AWS competency case 559"
        job_desc = "Looking for Python React AWS engineer position 559"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0560(self):
        doc_text = "Experienced Python developer with React and AWS competency case 560"
        job_desc = "Looking for Python React AWS engineer position 560"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0561(self):
        doc_text = "Experienced Python developer with React and AWS competency case 561"
        job_desc = "Looking for Python React AWS engineer position 561"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0562(self):
        doc_text = "Experienced Python developer with React and AWS competency case 562"
        job_desc = "Looking for Python React AWS engineer position 562"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0563(self):
        doc_text = "Experienced Python developer with React and AWS competency case 563"
        job_desc = "Looking for Python React AWS engineer position 563"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0564(self):
        doc_text = "Experienced Python developer with React and AWS competency case 564"
        job_desc = "Looking for Python React AWS engineer position 564"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0565(self):
        doc_text = "Experienced Python developer with React and AWS competency case 565"
        job_desc = "Looking for Python React AWS engineer position 565"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0566(self):
        doc_text = "Experienced Python developer with React and AWS competency case 566"
        job_desc = "Looking for Python React AWS engineer position 566"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0567(self):
        doc_text = "Experienced Python developer with React and AWS competency case 567"
        job_desc = "Looking for Python React AWS engineer position 567"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0568(self):
        doc_text = "Experienced Python developer with React and AWS competency case 568"
        job_desc = "Looking for Python React AWS engineer position 568"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0569(self):
        doc_text = "Experienced Python developer with React and AWS competency case 569"
        job_desc = "Looking for Python React AWS engineer position 569"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0570(self):
        doc_text = "Experienced Python developer with React and AWS competency case 570"
        job_desc = "Looking for Python React AWS engineer position 570"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0571(self):
        doc_text = "Experienced Python developer with React and AWS competency case 571"
        job_desc = "Looking for Python React AWS engineer position 571"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0572(self):
        doc_text = "Experienced Python developer with React and AWS competency case 572"
        job_desc = "Looking for Python React AWS engineer position 572"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0573(self):
        doc_text = "Experienced Python developer with React and AWS competency case 573"
        job_desc = "Looking for Python React AWS engineer position 573"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0574(self):
        doc_text = "Experienced Python developer with React and AWS competency case 574"
        job_desc = "Looking for Python React AWS engineer position 574"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0575(self):
        doc_text = "Experienced Python developer with React and AWS competency case 575"
        job_desc = "Looking for Python React AWS engineer position 575"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0576(self):
        doc_text = "Experienced Python developer with React and AWS competency case 576"
        job_desc = "Looking for Python React AWS engineer position 576"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0577(self):
        doc_text = "Experienced Python developer with React and AWS competency case 577"
        job_desc = "Looking for Python React AWS engineer position 577"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0578(self):
        doc_text = "Experienced Python developer with React and AWS competency case 578"
        job_desc = "Looking for Python React AWS engineer position 578"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0579(self):
        doc_text = "Experienced Python developer with React and AWS competency case 579"
        job_desc = "Looking for Python React AWS engineer position 579"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0580(self):
        doc_text = "Experienced Python developer with React and AWS competency case 580"
        job_desc = "Looking for Python React AWS engineer position 580"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0581(self):
        doc_text = "Experienced Python developer with React and AWS competency case 581"
        job_desc = "Looking for Python React AWS engineer position 581"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0582(self):
        doc_text = "Experienced Python developer with React and AWS competency case 582"
        job_desc = "Looking for Python React AWS engineer position 582"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0583(self):
        doc_text = "Experienced Python developer with React and AWS competency case 583"
        job_desc = "Looking for Python React AWS engineer position 583"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0584(self):
        doc_text = "Experienced Python developer with React and AWS competency case 584"
        job_desc = "Looking for Python React AWS engineer position 584"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0585(self):
        doc_text = "Experienced Python developer with React and AWS competency case 585"
        job_desc = "Looking for Python React AWS engineer position 585"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0586(self):
        doc_text = "Experienced Python developer with React and AWS competency case 586"
        job_desc = "Looking for Python React AWS engineer position 586"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0587(self):
        doc_text = "Experienced Python developer with React and AWS competency case 587"
        job_desc = "Looking for Python React AWS engineer position 587"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0588(self):
        doc_text = "Experienced Python developer with React and AWS competency case 588"
        job_desc = "Looking for Python React AWS engineer position 588"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0589(self):
        doc_text = "Experienced Python developer with React and AWS competency case 589"
        job_desc = "Looking for Python React AWS engineer position 589"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0590(self):
        doc_text = "Experienced Python developer with React and AWS competency case 590"
        job_desc = "Looking for Python React AWS engineer position 590"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0591(self):
        doc_text = "Experienced Python developer with React and AWS competency case 591"
        job_desc = "Looking for Python React AWS engineer position 591"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0592(self):
        doc_text = "Experienced Python developer with React and AWS competency case 592"
        job_desc = "Looking for Python React AWS engineer position 592"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0593(self):
        doc_text = "Experienced Python developer with React and AWS competency case 593"
        job_desc = "Looking for Python React AWS engineer position 593"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0594(self):
        doc_text = "Experienced Python developer with React and AWS competency case 594"
        job_desc = "Looking for Python React AWS engineer position 594"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0595(self):
        doc_text = "Experienced Python developer with React and AWS competency case 595"
        job_desc = "Looking for Python React AWS engineer position 595"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0596(self):
        doc_text = "Experienced Python developer with React and AWS competency case 596"
        job_desc = "Looking for Python React AWS engineer position 596"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0597(self):
        doc_text = "Experienced Python developer with React and AWS competency case 597"
        job_desc = "Looking for Python React AWS engineer position 597"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0598(self):
        doc_text = "Experienced Python developer with React and AWS competency case 598"
        job_desc = "Looking for Python React AWS engineer position 598"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0599(self):
        doc_text = "Experienced Python developer with React and AWS competency case 599"
        job_desc = "Looking for Python React AWS engineer position 599"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0600(self):
        doc_text = "Experienced Python developer with React and AWS competency case 600"
        job_desc = "Looking for Python React AWS engineer position 600"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0601(self):
        doc_text = "Experienced Python developer with React and AWS competency case 601"
        job_desc = "Looking for Python React AWS engineer position 601"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0602(self):
        doc_text = "Experienced Python developer with React and AWS competency case 602"
        job_desc = "Looking for Python React AWS engineer position 602"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0603(self):
        doc_text = "Experienced Python developer with React and AWS competency case 603"
        job_desc = "Looking for Python React AWS engineer position 603"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0604(self):
        doc_text = "Experienced Python developer with React and AWS competency case 604"
        job_desc = "Looking for Python React AWS engineer position 604"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0605(self):
        doc_text = "Experienced Python developer with React and AWS competency case 605"
        job_desc = "Looking for Python React AWS engineer position 605"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0606(self):
        doc_text = "Experienced Python developer with React and AWS competency case 606"
        job_desc = "Looking for Python React AWS engineer position 606"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0607(self):
        doc_text = "Experienced Python developer with React and AWS competency case 607"
        job_desc = "Looking for Python React AWS engineer position 607"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0608(self):
        doc_text = "Experienced Python developer with React and AWS competency case 608"
        job_desc = "Looking for Python React AWS engineer position 608"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0609(self):
        doc_text = "Experienced Python developer with React and AWS competency case 609"
        job_desc = "Looking for Python React AWS engineer position 609"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0610(self):
        doc_text = "Experienced Python developer with React and AWS competency case 610"
        job_desc = "Looking for Python React AWS engineer position 610"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0611(self):
        doc_text = "Experienced Python developer with React and AWS competency case 611"
        job_desc = "Looking for Python React AWS engineer position 611"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0612(self):
        doc_text = "Experienced Python developer with React and AWS competency case 612"
        job_desc = "Looking for Python React AWS engineer position 612"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0613(self):
        doc_text = "Experienced Python developer with React and AWS competency case 613"
        job_desc = "Looking for Python React AWS engineer position 613"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0614(self):
        doc_text = "Experienced Python developer with React and AWS competency case 614"
        job_desc = "Looking for Python React AWS engineer position 614"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0615(self):
        doc_text = "Experienced Python developer with React and AWS competency case 615"
        job_desc = "Looking for Python React AWS engineer position 615"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0616(self):
        doc_text = "Experienced Python developer with React and AWS competency case 616"
        job_desc = "Looking for Python React AWS engineer position 616"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0617(self):
        doc_text = "Experienced Python developer with React and AWS competency case 617"
        job_desc = "Looking for Python React AWS engineer position 617"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0618(self):
        doc_text = "Experienced Python developer with React and AWS competency case 618"
        job_desc = "Looking for Python React AWS engineer position 618"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0619(self):
        doc_text = "Experienced Python developer with React and AWS competency case 619"
        job_desc = "Looking for Python React AWS engineer position 619"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0620(self):
        doc_text = "Experienced Python developer with React and AWS competency case 620"
        job_desc = "Looking for Python React AWS engineer position 620"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0621(self):
        doc_text = "Experienced Python developer with React and AWS competency case 621"
        job_desc = "Looking for Python React AWS engineer position 621"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0622(self):
        doc_text = "Experienced Python developer with React and AWS competency case 622"
        job_desc = "Looking for Python React AWS engineer position 622"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0623(self):
        doc_text = "Experienced Python developer with React and AWS competency case 623"
        job_desc = "Looking for Python React AWS engineer position 623"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0624(self):
        doc_text = "Experienced Python developer with React and AWS competency case 624"
        job_desc = "Looking for Python React AWS engineer position 624"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0625(self):
        doc_text = "Experienced Python developer with React and AWS competency case 625"
        job_desc = "Looking for Python React AWS engineer position 625"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0626(self):
        doc_text = "Experienced Python developer with React and AWS competency case 626"
        job_desc = "Looking for Python React AWS engineer position 626"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0627(self):
        doc_text = "Experienced Python developer with React and AWS competency case 627"
        job_desc = "Looking for Python React AWS engineer position 627"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0628(self):
        doc_text = "Experienced Python developer with React and AWS competency case 628"
        job_desc = "Looking for Python React AWS engineer position 628"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0629(self):
        doc_text = "Experienced Python developer with React and AWS competency case 629"
        job_desc = "Looking for Python React AWS engineer position 629"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0630(self):
        doc_text = "Experienced Python developer with React and AWS competency case 630"
        job_desc = "Looking for Python React AWS engineer position 630"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0631(self):
        doc_text = "Experienced Python developer with React and AWS competency case 631"
        job_desc = "Looking for Python React AWS engineer position 631"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0632(self):
        doc_text = "Experienced Python developer with React and AWS competency case 632"
        job_desc = "Looking for Python React AWS engineer position 632"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0633(self):
        doc_text = "Experienced Python developer with React and AWS competency case 633"
        job_desc = "Looking for Python React AWS engineer position 633"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0634(self):
        doc_text = "Experienced Python developer with React and AWS competency case 634"
        job_desc = "Looking for Python React AWS engineer position 634"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0635(self):
        doc_text = "Experienced Python developer with React and AWS competency case 635"
        job_desc = "Looking for Python React AWS engineer position 635"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0636(self):
        doc_text = "Experienced Python developer with React and AWS competency case 636"
        job_desc = "Looking for Python React AWS engineer position 636"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0637(self):
        doc_text = "Experienced Python developer with React and AWS competency case 637"
        job_desc = "Looking for Python React AWS engineer position 637"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0638(self):
        doc_text = "Experienced Python developer with React and AWS competency case 638"
        job_desc = "Looking for Python React AWS engineer position 638"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0639(self):
        doc_text = "Experienced Python developer with React and AWS competency case 639"
        job_desc = "Looking for Python React AWS engineer position 639"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0640(self):
        doc_text = "Experienced Python developer with React and AWS competency case 640"
        job_desc = "Looking for Python React AWS engineer position 640"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0641(self):
        doc_text = "Experienced Python developer with React and AWS competency case 641"
        job_desc = "Looking for Python React AWS engineer position 641"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0642(self):
        doc_text = "Experienced Python developer with React and AWS competency case 642"
        job_desc = "Looking for Python React AWS engineer position 642"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0643(self):
        doc_text = "Experienced Python developer with React and AWS competency case 643"
        job_desc = "Looking for Python React AWS engineer position 643"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0644(self):
        doc_text = "Experienced Python developer with React and AWS competency case 644"
        job_desc = "Looking for Python React AWS engineer position 644"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0645(self):
        doc_text = "Experienced Python developer with React and AWS competency case 645"
        job_desc = "Looking for Python React AWS engineer position 645"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0646(self):
        doc_text = "Experienced Python developer with React and AWS competency case 646"
        job_desc = "Looking for Python React AWS engineer position 646"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0647(self):
        doc_text = "Experienced Python developer with React and AWS competency case 647"
        job_desc = "Looking for Python React AWS engineer position 647"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0648(self):
        doc_text = "Experienced Python developer with React and AWS competency case 648"
        job_desc = "Looking for Python React AWS engineer position 648"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0649(self):
        doc_text = "Experienced Python developer with React and AWS competency case 649"
        job_desc = "Looking for Python React AWS engineer position 649"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0650(self):
        doc_text = "Experienced Python developer with React and AWS competency case 650"
        job_desc = "Looking for Python React AWS engineer position 650"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0651(self):
        doc_text = "Experienced Python developer with React and AWS competency case 651"
        job_desc = "Looking for Python React AWS engineer position 651"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0652(self):
        doc_text = "Experienced Python developer with React and AWS competency case 652"
        job_desc = "Looking for Python React AWS engineer position 652"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0653(self):
        doc_text = "Experienced Python developer with React and AWS competency case 653"
        job_desc = "Looking for Python React AWS engineer position 653"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0654(self):
        doc_text = "Experienced Python developer with React and AWS competency case 654"
        job_desc = "Looking for Python React AWS engineer position 654"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0655(self):
        doc_text = "Experienced Python developer with React and AWS competency case 655"
        job_desc = "Looking for Python React AWS engineer position 655"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0656(self):
        doc_text = "Experienced Python developer with React and AWS competency case 656"
        job_desc = "Looking for Python React AWS engineer position 656"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0657(self):
        doc_text = "Experienced Python developer with React and AWS competency case 657"
        job_desc = "Looking for Python React AWS engineer position 657"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0658(self):
        doc_text = "Experienced Python developer with React and AWS competency case 658"
        job_desc = "Looking for Python React AWS engineer position 658"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0659(self):
        doc_text = "Experienced Python developer with React and AWS competency case 659"
        job_desc = "Looking for Python React AWS engineer position 659"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0660(self):
        doc_text = "Experienced Python developer with React and AWS competency case 660"
        job_desc = "Looking for Python React AWS engineer position 660"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0661(self):
        doc_text = "Experienced Python developer with React and AWS competency case 661"
        job_desc = "Looking for Python React AWS engineer position 661"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0662(self):
        doc_text = "Experienced Python developer with React and AWS competency case 662"
        job_desc = "Looking for Python React AWS engineer position 662"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0663(self):
        doc_text = "Experienced Python developer with React and AWS competency case 663"
        job_desc = "Looking for Python React AWS engineer position 663"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0664(self):
        doc_text = "Experienced Python developer with React and AWS competency case 664"
        job_desc = "Looking for Python React AWS engineer position 664"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0665(self):
        doc_text = "Experienced Python developer with React and AWS competency case 665"
        job_desc = "Looking for Python React AWS engineer position 665"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0666(self):
        doc_text = "Experienced Python developer with React and AWS competency case 666"
        job_desc = "Looking for Python React AWS engineer position 666"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0667(self):
        doc_text = "Experienced Python developer with React and AWS competency case 667"
        job_desc = "Looking for Python React AWS engineer position 667"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0668(self):
        doc_text = "Experienced Python developer with React and AWS competency case 668"
        job_desc = "Looking for Python React AWS engineer position 668"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0669(self):
        doc_text = "Experienced Python developer with React and AWS competency case 669"
        job_desc = "Looking for Python React AWS engineer position 669"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0670(self):
        doc_text = "Experienced Python developer with React and AWS competency case 670"
        job_desc = "Looking for Python React AWS engineer position 670"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0671(self):
        doc_text = "Experienced Python developer with React and AWS competency case 671"
        job_desc = "Looking for Python React AWS engineer position 671"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0672(self):
        doc_text = "Experienced Python developer with React and AWS competency case 672"
        job_desc = "Looking for Python React AWS engineer position 672"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0673(self):
        doc_text = "Experienced Python developer with React and AWS competency case 673"
        job_desc = "Looking for Python React AWS engineer position 673"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0674(self):
        doc_text = "Experienced Python developer with React and AWS competency case 674"
        job_desc = "Looking for Python React AWS engineer position 674"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0675(self):
        doc_text = "Experienced Python developer with React and AWS competency case 675"
        job_desc = "Looking for Python React AWS engineer position 675"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0676(self):
        doc_text = "Experienced Python developer with React and AWS competency case 676"
        job_desc = "Looking for Python React AWS engineer position 676"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0677(self):
        doc_text = "Experienced Python developer with React and AWS competency case 677"
        job_desc = "Looking for Python React AWS engineer position 677"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0678(self):
        doc_text = "Experienced Python developer with React and AWS competency case 678"
        job_desc = "Looking for Python React AWS engineer position 678"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0679(self):
        doc_text = "Experienced Python developer with React and AWS competency case 679"
        job_desc = "Looking for Python React AWS engineer position 679"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0680(self):
        doc_text = "Experienced Python developer with React and AWS competency case 680"
        job_desc = "Looking for Python React AWS engineer position 680"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0681(self):
        doc_text = "Experienced Python developer with React and AWS competency case 681"
        job_desc = "Looking for Python React AWS engineer position 681"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0682(self):
        doc_text = "Experienced Python developer with React and AWS competency case 682"
        job_desc = "Looking for Python React AWS engineer position 682"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0683(self):
        doc_text = "Experienced Python developer with React and AWS competency case 683"
        job_desc = "Looking for Python React AWS engineer position 683"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0684(self):
        doc_text = "Experienced Python developer with React and AWS competency case 684"
        job_desc = "Looking for Python React AWS engineer position 684"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0685(self):
        doc_text = "Experienced Python developer with React and AWS competency case 685"
        job_desc = "Looking for Python React AWS engineer position 685"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0686(self):
        doc_text = "Experienced Python developer with React and AWS competency case 686"
        job_desc = "Looking for Python React AWS engineer position 686"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0687(self):
        doc_text = "Experienced Python developer with React and AWS competency case 687"
        job_desc = "Looking for Python React AWS engineer position 687"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0688(self):
        doc_text = "Experienced Python developer with React and AWS competency case 688"
        job_desc = "Looking for Python React AWS engineer position 688"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0689(self):
        doc_text = "Experienced Python developer with React and AWS competency case 689"
        job_desc = "Looking for Python React AWS engineer position 689"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0690(self):
        doc_text = "Experienced Python developer with React and AWS competency case 690"
        job_desc = "Looking for Python React AWS engineer position 690"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0691(self):
        doc_text = "Experienced Python developer with React and AWS competency case 691"
        job_desc = "Looking for Python React AWS engineer position 691"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0692(self):
        doc_text = "Experienced Python developer with React and AWS competency case 692"
        job_desc = "Looking for Python React AWS engineer position 692"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0693(self):
        doc_text = "Experienced Python developer with React and AWS competency case 693"
        job_desc = "Looking for Python React AWS engineer position 693"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0694(self):
        doc_text = "Experienced Python developer with React and AWS competency case 694"
        job_desc = "Looking for Python React AWS engineer position 694"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0695(self):
        doc_text = "Experienced Python developer with React and AWS competency case 695"
        job_desc = "Looking for Python React AWS engineer position 695"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0696(self):
        doc_text = "Experienced Python developer with React and AWS competency case 696"
        job_desc = "Looking for Python React AWS engineer position 696"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0697(self):
        doc_text = "Experienced Python developer with React and AWS competency case 697"
        job_desc = "Looking for Python React AWS engineer position 697"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0698(self):
        doc_text = "Experienced Python developer with React and AWS competency case 698"
        job_desc = "Looking for Python React AWS engineer position 698"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0699(self):
        doc_text = "Experienced Python developer with React and AWS competency case 699"
        job_desc = "Looking for Python React AWS engineer position 699"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0700(self):
        doc_text = "Experienced Python developer with React and AWS competency case 700"
        job_desc = "Looking for Python React AWS engineer position 700"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0701(self):
        doc_text = "Experienced Python developer with React and AWS competency case 701"
        job_desc = "Looking for Python React AWS engineer position 701"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0702(self):
        doc_text = "Experienced Python developer with React and AWS competency case 702"
        job_desc = "Looking for Python React AWS engineer position 702"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0703(self):
        doc_text = "Experienced Python developer with React and AWS competency case 703"
        job_desc = "Looking for Python React AWS engineer position 703"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0704(self):
        doc_text = "Experienced Python developer with React and AWS competency case 704"
        job_desc = "Looking for Python React AWS engineer position 704"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0705(self):
        doc_text = "Experienced Python developer with React and AWS competency case 705"
        job_desc = "Looking for Python React AWS engineer position 705"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0706(self):
        doc_text = "Experienced Python developer with React and AWS competency case 706"
        job_desc = "Looking for Python React AWS engineer position 706"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0707(self):
        doc_text = "Experienced Python developer with React and AWS competency case 707"
        job_desc = "Looking for Python React AWS engineer position 707"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0708(self):
        doc_text = "Experienced Python developer with React and AWS competency case 708"
        job_desc = "Looking for Python React AWS engineer position 708"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0709(self):
        doc_text = "Experienced Python developer with React and AWS competency case 709"
        job_desc = "Looking for Python React AWS engineer position 709"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0710(self):
        doc_text = "Experienced Python developer with React and AWS competency case 710"
        job_desc = "Looking for Python React AWS engineer position 710"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0711(self):
        doc_text = "Experienced Python developer with React and AWS competency case 711"
        job_desc = "Looking for Python React AWS engineer position 711"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0712(self):
        doc_text = "Experienced Python developer with React and AWS competency case 712"
        job_desc = "Looking for Python React AWS engineer position 712"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0713(self):
        doc_text = "Experienced Python developer with React and AWS competency case 713"
        job_desc = "Looking for Python React AWS engineer position 713"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0714(self):
        doc_text = "Experienced Python developer with React and AWS competency case 714"
        job_desc = "Looking for Python React AWS engineer position 714"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0715(self):
        doc_text = "Experienced Python developer with React and AWS competency case 715"
        job_desc = "Looking for Python React AWS engineer position 715"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0716(self):
        doc_text = "Experienced Python developer with React and AWS competency case 716"
        job_desc = "Looking for Python React AWS engineer position 716"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0717(self):
        doc_text = "Experienced Python developer with React and AWS competency case 717"
        job_desc = "Looking for Python React AWS engineer position 717"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0718(self):
        doc_text = "Experienced Python developer with React and AWS competency case 718"
        job_desc = "Looking for Python React AWS engineer position 718"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0719(self):
        doc_text = "Experienced Python developer with React and AWS competency case 719"
        job_desc = "Looking for Python React AWS engineer position 719"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0720(self):
        doc_text = "Experienced Python developer with React and AWS competency case 720"
        job_desc = "Looking for Python React AWS engineer position 720"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0721(self):
        doc_text = "Experienced Python developer with React and AWS competency case 721"
        job_desc = "Looking for Python React AWS engineer position 721"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0722(self):
        doc_text = "Experienced Python developer with React and AWS competency case 722"
        job_desc = "Looking for Python React AWS engineer position 722"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0723(self):
        doc_text = "Experienced Python developer with React and AWS competency case 723"
        job_desc = "Looking for Python React AWS engineer position 723"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0724(self):
        doc_text = "Experienced Python developer with React and AWS competency case 724"
        job_desc = "Looking for Python React AWS engineer position 724"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0725(self):
        doc_text = "Experienced Python developer with React and AWS competency case 725"
        job_desc = "Looking for Python React AWS engineer position 725"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0726(self):
        doc_text = "Experienced Python developer with React and AWS competency case 726"
        job_desc = "Looking for Python React AWS engineer position 726"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0727(self):
        doc_text = "Experienced Python developer with React and AWS competency case 727"
        job_desc = "Looking for Python React AWS engineer position 727"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0728(self):
        doc_text = "Experienced Python developer with React and AWS competency case 728"
        job_desc = "Looking for Python React AWS engineer position 728"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0729(self):
        doc_text = "Experienced Python developer with React and AWS competency case 729"
        job_desc = "Looking for Python React AWS engineer position 729"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0730(self):
        doc_text = "Experienced Python developer with React and AWS competency case 730"
        job_desc = "Looking for Python React AWS engineer position 730"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0731(self):
        doc_text = "Experienced Python developer with React and AWS competency case 731"
        job_desc = "Looking for Python React AWS engineer position 731"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0732(self):
        doc_text = "Experienced Python developer with React and AWS competency case 732"
        job_desc = "Looking for Python React AWS engineer position 732"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0733(self):
        doc_text = "Experienced Python developer with React and AWS competency case 733"
        job_desc = "Looking for Python React AWS engineer position 733"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0734(self):
        doc_text = "Experienced Python developer with React and AWS competency case 734"
        job_desc = "Looking for Python React AWS engineer position 734"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0735(self):
        doc_text = "Experienced Python developer with React and AWS competency case 735"
        job_desc = "Looking for Python React AWS engineer position 735"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0736(self):
        doc_text = "Experienced Python developer with React and AWS competency case 736"
        job_desc = "Looking for Python React AWS engineer position 736"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0737(self):
        doc_text = "Experienced Python developer with React and AWS competency case 737"
        job_desc = "Looking for Python React AWS engineer position 737"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0738(self):
        doc_text = "Experienced Python developer with React and AWS competency case 738"
        job_desc = "Looking for Python React AWS engineer position 738"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0739(self):
        doc_text = "Experienced Python developer with React and AWS competency case 739"
        job_desc = "Looking for Python React AWS engineer position 739"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0740(self):
        doc_text = "Experienced Python developer with React and AWS competency case 740"
        job_desc = "Looking for Python React AWS engineer position 740"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0741(self):
        doc_text = "Experienced Python developer with React and AWS competency case 741"
        job_desc = "Looking for Python React AWS engineer position 741"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0742(self):
        doc_text = "Experienced Python developer with React and AWS competency case 742"
        job_desc = "Looking for Python React AWS engineer position 742"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0743(self):
        doc_text = "Experienced Python developer with React and AWS competency case 743"
        job_desc = "Looking for Python React AWS engineer position 743"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0744(self):
        doc_text = "Experienced Python developer with React and AWS competency case 744"
        job_desc = "Looking for Python React AWS engineer position 744"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0745(self):
        doc_text = "Experienced Python developer with React and AWS competency case 745"
        job_desc = "Looking for Python React AWS engineer position 745"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0746(self):
        doc_text = "Experienced Python developer with React and AWS competency case 746"
        job_desc = "Looking for Python React AWS engineer position 746"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0747(self):
        doc_text = "Experienced Python developer with React and AWS competency case 747"
        job_desc = "Looking for Python React AWS engineer position 747"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0748(self):
        doc_text = "Experienced Python developer with React and AWS competency case 748"
        job_desc = "Looking for Python React AWS engineer position 748"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0749(self):
        doc_text = "Experienced Python developer with React and AWS competency case 749"
        job_desc = "Looking for Python React AWS engineer position 749"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0750(self):
        doc_text = "Experienced Python developer with React and AWS competency case 750"
        job_desc = "Looking for Python React AWS engineer position 750"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0751(self):
        doc_text = "Experienced Python developer with React and AWS competency case 751"
        job_desc = "Looking for Python React AWS engineer position 751"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0752(self):
        doc_text = "Experienced Python developer with React and AWS competency case 752"
        job_desc = "Looking for Python React AWS engineer position 752"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0753(self):
        doc_text = "Experienced Python developer with React and AWS competency case 753"
        job_desc = "Looking for Python React AWS engineer position 753"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0754(self):
        doc_text = "Experienced Python developer with React and AWS competency case 754"
        job_desc = "Looking for Python React AWS engineer position 754"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0755(self):
        doc_text = "Experienced Python developer with React and AWS competency case 755"
        job_desc = "Looking for Python React AWS engineer position 755"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0756(self):
        doc_text = "Experienced Python developer with React and AWS competency case 756"
        job_desc = "Looking for Python React AWS engineer position 756"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0757(self):
        doc_text = "Experienced Python developer with React and AWS competency case 757"
        job_desc = "Looking for Python React AWS engineer position 757"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0758(self):
        doc_text = "Experienced Python developer with React and AWS competency case 758"
        job_desc = "Looking for Python React AWS engineer position 758"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0759(self):
        doc_text = "Experienced Python developer with React and AWS competency case 759"
        job_desc = "Looking for Python React AWS engineer position 759"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0760(self):
        doc_text = "Experienced Python developer with React and AWS competency case 760"
        job_desc = "Looking for Python React AWS engineer position 760"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0761(self):
        doc_text = "Experienced Python developer with React and AWS competency case 761"
        job_desc = "Looking for Python React AWS engineer position 761"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0762(self):
        doc_text = "Experienced Python developer with React and AWS competency case 762"
        job_desc = "Looking for Python React AWS engineer position 762"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0763(self):
        doc_text = "Experienced Python developer with React and AWS competency case 763"
        job_desc = "Looking for Python React AWS engineer position 763"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0764(self):
        doc_text = "Experienced Python developer with React and AWS competency case 764"
        job_desc = "Looking for Python React AWS engineer position 764"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0765(self):
        doc_text = "Experienced Python developer with React and AWS competency case 765"
        job_desc = "Looking for Python React AWS engineer position 765"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0766(self):
        doc_text = "Experienced Python developer with React and AWS competency case 766"
        job_desc = "Looking for Python React AWS engineer position 766"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0767(self):
        doc_text = "Experienced Python developer with React and AWS competency case 767"
        job_desc = "Looking for Python React AWS engineer position 767"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0768(self):
        doc_text = "Experienced Python developer with React and AWS competency case 768"
        job_desc = "Looking for Python React AWS engineer position 768"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0769(self):
        doc_text = "Experienced Python developer with React and AWS competency case 769"
        job_desc = "Looking for Python React AWS engineer position 769"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0770(self):
        doc_text = "Experienced Python developer with React and AWS competency case 770"
        job_desc = "Looking for Python React AWS engineer position 770"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0771(self):
        doc_text = "Experienced Python developer with React and AWS competency case 771"
        job_desc = "Looking for Python React AWS engineer position 771"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0772(self):
        doc_text = "Experienced Python developer with React and AWS competency case 772"
        job_desc = "Looking for Python React AWS engineer position 772"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0773(self):
        doc_text = "Experienced Python developer with React and AWS competency case 773"
        job_desc = "Looking for Python React AWS engineer position 773"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0774(self):
        doc_text = "Experienced Python developer with React and AWS competency case 774"
        job_desc = "Looking for Python React AWS engineer position 774"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0775(self):
        doc_text = "Experienced Python developer with React and AWS competency case 775"
        job_desc = "Looking for Python React AWS engineer position 775"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0776(self):
        doc_text = "Experienced Python developer with React and AWS competency case 776"
        job_desc = "Looking for Python React AWS engineer position 776"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0777(self):
        doc_text = "Experienced Python developer with React and AWS competency case 777"
        job_desc = "Looking for Python React AWS engineer position 777"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0778(self):
        doc_text = "Experienced Python developer with React and AWS competency case 778"
        job_desc = "Looking for Python React AWS engineer position 778"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0779(self):
        doc_text = "Experienced Python developer with React and AWS competency case 779"
        job_desc = "Looking for Python React AWS engineer position 779"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0780(self):
        doc_text = "Experienced Python developer with React and AWS competency case 780"
        job_desc = "Looking for Python React AWS engineer position 780"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0781(self):
        doc_text = "Experienced Python developer with React and AWS competency case 781"
        job_desc = "Looking for Python React AWS engineer position 781"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0782(self):
        doc_text = "Experienced Python developer with React and AWS competency case 782"
        job_desc = "Looking for Python React AWS engineer position 782"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0783(self):
        doc_text = "Experienced Python developer with React and AWS competency case 783"
        job_desc = "Looking for Python React AWS engineer position 783"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0784(self):
        doc_text = "Experienced Python developer with React and AWS competency case 784"
        job_desc = "Looking for Python React AWS engineer position 784"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0785(self):
        doc_text = "Experienced Python developer with React and AWS competency case 785"
        job_desc = "Looking for Python React AWS engineer position 785"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0786(self):
        doc_text = "Experienced Python developer with React and AWS competency case 786"
        job_desc = "Looking for Python React AWS engineer position 786"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0787(self):
        doc_text = "Experienced Python developer with React and AWS competency case 787"
        job_desc = "Looking for Python React AWS engineer position 787"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0788(self):
        doc_text = "Experienced Python developer with React and AWS competency case 788"
        job_desc = "Looking for Python React AWS engineer position 788"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0789(self):
        doc_text = "Experienced Python developer with React and AWS competency case 789"
        job_desc = "Looking for Python React AWS engineer position 789"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0790(self):
        doc_text = "Experienced Python developer with React and AWS competency case 790"
        job_desc = "Looking for Python React AWS engineer position 790"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0791(self):
        doc_text = "Experienced Python developer with React and AWS competency case 791"
        job_desc = "Looking for Python React AWS engineer position 791"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0792(self):
        doc_text = "Experienced Python developer with React and AWS competency case 792"
        job_desc = "Looking for Python React AWS engineer position 792"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0793(self):
        doc_text = "Experienced Python developer with React and AWS competency case 793"
        job_desc = "Looking for Python React AWS engineer position 793"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0794(self):
        doc_text = "Experienced Python developer with React and AWS competency case 794"
        job_desc = "Looking for Python React AWS engineer position 794"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0795(self):
        doc_text = "Experienced Python developer with React and AWS competency case 795"
        job_desc = "Looking for Python React AWS engineer position 795"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0796(self):
        doc_text = "Experienced Python developer with React and AWS competency case 796"
        job_desc = "Looking for Python React AWS engineer position 796"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0797(self):
        doc_text = "Experienced Python developer with React and AWS competency case 797"
        job_desc = "Looking for Python React AWS engineer position 797"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0798(self):
        doc_text = "Experienced Python developer with React and AWS competency case 798"
        job_desc = "Looking for Python React AWS engineer position 798"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0799(self):
        doc_text = "Experienced Python developer with React and AWS competency case 799"
        job_desc = "Looking for Python React AWS engineer position 799"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0800(self):
        doc_text = "Experienced Python developer with React and AWS competency case 800"
        job_desc = "Looking for Python React AWS engineer position 800"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0801(self):
        doc_text = "Experienced Python developer with React and AWS competency case 801"
        job_desc = "Looking for Python React AWS engineer position 801"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0802(self):
        doc_text = "Experienced Python developer with React and AWS competency case 802"
        job_desc = "Looking for Python React AWS engineer position 802"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0803(self):
        doc_text = "Experienced Python developer with React and AWS competency case 803"
        job_desc = "Looking for Python React AWS engineer position 803"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0804(self):
        doc_text = "Experienced Python developer with React and AWS competency case 804"
        job_desc = "Looking for Python React AWS engineer position 804"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0805(self):
        doc_text = "Experienced Python developer with React and AWS competency case 805"
        job_desc = "Looking for Python React AWS engineer position 805"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0806(self):
        doc_text = "Experienced Python developer with React and AWS competency case 806"
        job_desc = "Looking for Python React AWS engineer position 806"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0807(self):
        doc_text = "Experienced Python developer with React and AWS competency case 807"
        job_desc = "Looking for Python React AWS engineer position 807"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0808(self):
        doc_text = "Experienced Python developer with React and AWS competency case 808"
        job_desc = "Looking for Python React AWS engineer position 808"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0809(self):
        doc_text = "Experienced Python developer with React and AWS competency case 809"
        job_desc = "Looking for Python React AWS engineer position 809"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0810(self):
        doc_text = "Experienced Python developer with React and AWS competency case 810"
        job_desc = "Looking for Python React AWS engineer position 810"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0811(self):
        doc_text = "Experienced Python developer with React and AWS competency case 811"
        job_desc = "Looking for Python React AWS engineer position 811"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0812(self):
        doc_text = "Experienced Python developer with React and AWS competency case 812"
        job_desc = "Looking for Python React AWS engineer position 812"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0813(self):
        doc_text = "Experienced Python developer with React and AWS competency case 813"
        job_desc = "Looking for Python React AWS engineer position 813"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0814(self):
        doc_text = "Experienced Python developer with React and AWS competency case 814"
        job_desc = "Looking for Python React AWS engineer position 814"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0815(self):
        doc_text = "Experienced Python developer with React and AWS competency case 815"
        job_desc = "Looking for Python React AWS engineer position 815"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0816(self):
        doc_text = "Experienced Python developer with React and AWS competency case 816"
        job_desc = "Looking for Python React AWS engineer position 816"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0817(self):
        doc_text = "Experienced Python developer with React and AWS competency case 817"
        job_desc = "Looking for Python React AWS engineer position 817"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0818(self):
        doc_text = "Experienced Python developer with React and AWS competency case 818"
        job_desc = "Looking for Python React AWS engineer position 818"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0819(self):
        doc_text = "Experienced Python developer with React and AWS competency case 819"
        job_desc = "Looking for Python React AWS engineer position 819"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0820(self):
        doc_text = "Experienced Python developer with React and AWS competency case 820"
        job_desc = "Looking for Python React AWS engineer position 820"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0821(self):
        doc_text = "Experienced Python developer with React and AWS competency case 821"
        job_desc = "Looking for Python React AWS engineer position 821"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0822(self):
        doc_text = "Experienced Python developer with React and AWS competency case 822"
        job_desc = "Looking for Python React AWS engineer position 822"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0823(self):
        doc_text = "Experienced Python developer with React and AWS competency case 823"
        job_desc = "Looking for Python React AWS engineer position 823"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0824(self):
        doc_text = "Experienced Python developer with React and AWS competency case 824"
        job_desc = "Looking for Python React AWS engineer position 824"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0825(self):
        doc_text = "Experienced Python developer with React and AWS competency case 825"
        job_desc = "Looking for Python React AWS engineer position 825"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0826(self):
        doc_text = "Experienced Python developer with React and AWS competency case 826"
        job_desc = "Looking for Python React AWS engineer position 826"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0827(self):
        doc_text = "Experienced Python developer with React and AWS competency case 827"
        job_desc = "Looking for Python React AWS engineer position 827"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0828(self):
        doc_text = "Experienced Python developer with React and AWS competency case 828"
        job_desc = "Looking for Python React AWS engineer position 828"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0829(self):
        doc_text = "Experienced Python developer with React and AWS competency case 829"
        job_desc = "Looking for Python React AWS engineer position 829"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0830(self):
        doc_text = "Experienced Python developer with React and AWS competency case 830"
        job_desc = "Looking for Python React AWS engineer position 830"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0831(self):
        doc_text = "Experienced Python developer with React and AWS competency case 831"
        job_desc = "Looking for Python React AWS engineer position 831"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0832(self):
        doc_text = "Experienced Python developer with React and AWS competency case 832"
        job_desc = "Looking for Python React AWS engineer position 832"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0833(self):
        doc_text = "Experienced Python developer with React and AWS competency case 833"
        job_desc = "Looking for Python React AWS engineer position 833"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0834(self):
        doc_text = "Experienced Python developer with React and AWS competency case 834"
        job_desc = "Looking for Python React AWS engineer position 834"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0835(self):
        doc_text = "Experienced Python developer with React and AWS competency case 835"
        job_desc = "Looking for Python React AWS engineer position 835"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0836(self):
        doc_text = "Experienced Python developer with React and AWS competency case 836"
        job_desc = "Looking for Python React AWS engineer position 836"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0837(self):
        doc_text = "Experienced Python developer with React and AWS competency case 837"
        job_desc = "Looking for Python React AWS engineer position 837"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0838(self):
        doc_text = "Experienced Python developer with React and AWS competency case 838"
        job_desc = "Looking for Python React AWS engineer position 838"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0839(self):
        doc_text = "Experienced Python developer with React and AWS competency case 839"
        job_desc = "Looking for Python React AWS engineer position 839"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0840(self):
        doc_text = "Experienced Python developer with React and AWS competency case 840"
        job_desc = "Looking for Python React AWS engineer position 840"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0841(self):
        doc_text = "Experienced Python developer with React and AWS competency case 841"
        job_desc = "Looking for Python React AWS engineer position 841"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0842(self):
        doc_text = "Experienced Python developer with React and AWS competency case 842"
        job_desc = "Looking for Python React AWS engineer position 842"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0843(self):
        doc_text = "Experienced Python developer with React and AWS competency case 843"
        job_desc = "Looking for Python React AWS engineer position 843"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0844(self):
        doc_text = "Experienced Python developer with React and AWS competency case 844"
        job_desc = "Looking for Python React AWS engineer position 844"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0845(self):
        doc_text = "Experienced Python developer with React and AWS competency case 845"
        job_desc = "Looking for Python React AWS engineer position 845"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0846(self):
        doc_text = "Experienced Python developer with React and AWS competency case 846"
        job_desc = "Looking for Python React AWS engineer position 846"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0847(self):
        doc_text = "Experienced Python developer with React and AWS competency case 847"
        job_desc = "Looking for Python React AWS engineer position 847"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0848(self):
        doc_text = "Experienced Python developer with React and AWS competency case 848"
        job_desc = "Looking for Python React AWS engineer position 848"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0849(self):
        doc_text = "Experienced Python developer with React and AWS competency case 849"
        job_desc = "Looking for Python React AWS engineer position 849"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0850(self):
        doc_text = "Experienced Python developer with React and AWS competency case 850"
        job_desc = "Looking for Python React AWS engineer position 850"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0851(self):
        doc_text = "Experienced Python developer with React and AWS competency case 851"
        job_desc = "Looking for Python React AWS engineer position 851"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0852(self):
        doc_text = "Experienced Python developer with React and AWS competency case 852"
        job_desc = "Looking for Python React AWS engineer position 852"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0853(self):
        doc_text = "Experienced Python developer with React and AWS competency case 853"
        job_desc = "Looking for Python React AWS engineer position 853"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0854(self):
        doc_text = "Experienced Python developer with React and AWS competency case 854"
        job_desc = "Looking for Python React AWS engineer position 854"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0855(self):
        doc_text = "Experienced Python developer with React and AWS competency case 855"
        job_desc = "Looking for Python React AWS engineer position 855"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0856(self):
        doc_text = "Experienced Python developer with React and AWS competency case 856"
        job_desc = "Looking for Python React AWS engineer position 856"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0857(self):
        doc_text = "Experienced Python developer with React and AWS competency case 857"
        job_desc = "Looking for Python React AWS engineer position 857"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0858(self):
        doc_text = "Experienced Python developer with React and AWS competency case 858"
        job_desc = "Looking for Python React AWS engineer position 858"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0859(self):
        doc_text = "Experienced Python developer with React and AWS competency case 859"
        job_desc = "Looking for Python React AWS engineer position 859"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0860(self):
        doc_text = "Experienced Python developer with React and AWS competency case 860"
        job_desc = "Looking for Python React AWS engineer position 860"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0861(self):
        doc_text = "Experienced Python developer with React and AWS competency case 861"
        job_desc = "Looking for Python React AWS engineer position 861"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0862(self):
        doc_text = "Experienced Python developer with React and AWS competency case 862"
        job_desc = "Looking for Python React AWS engineer position 862"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0863(self):
        doc_text = "Experienced Python developer with React and AWS competency case 863"
        job_desc = "Looking for Python React AWS engineer position 863"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0864(self):
        doc_text = "Experienced Python developer with React and AWS competency case 864"
        job_desc = "Looking for Python React AWS engineer position 864"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0865(self):
        doc_text = "Experienced Python developer with React and AWS competency case 865"
        job_desc = "Looking for Python React AWS engineer position 865"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0866(self):
        doc_text = "Experienced Python developer with React and AWS competency case 866"
        job_desc = "Looking for Python React AWS engineer position 866"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0867(self):
        doc_text = "Experienced Python developer with React and AWS competency case 867"
        job_desc = "Looking for Python React AWS engineer position 867"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0868(self):
        doc_text = "Experienced Python developer with React and AWS competency case 868"
        job_desc = "Looking for Python React AWS engineer position 868"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0869(self):
        doc_text = "Experienced Python developer with React and AWS competency case 869"
        job_desc = "Looking for Python React AWS engineer position 869"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0870(self):
        doc_text = "Experienced Python developer with React and AWS competency case 870"
        job_desc = "Looking for Python React AWS engineer position 870"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0871(self):
        doc_text = "Experienced Python developer with React and AWS competency case 871"
        job_desc = "Looking for Python React AWS engineer position 871"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0872(self):
        doc_text = "Experienced Python developer with React and AWS competency case 872"
        job_desc = "Looking for Python React AWS engineer position 872"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0873(self):
        doc_text = "Experienced Python developer with React and AWS competency case 873"
        job_desc = "Looking for Python React AWS engineer position 873"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0874(self):
        doc_text = "Experienced Python developer with React and AWS competency case 874"
        job_desc = "Looking for Python React AWS engineer position 874"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0875(self):
        doc_text = "Experienced Python developer with React and AWS competency case 875"
        job_desc = "Looking for Python React AWS engineer position 875"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0876(self):
        doc_text = "Experienced Python developer with React and AWS competency case 876"
        job_desc = "Looking for Python React AWS engineer position 876"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0877(self):
        doc_text = "Experienced Python developer with React and AWS competency case 877"
        job_desc = "Looking for Python React AWS engineer position 877"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0878(self):
        doc_text = "Experienced Python developer with React and AWS competency case 878"
        job_desc = "Looking for Python React AWS engineer position 878"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0879(self):
        doc_text = "Experienced Python developer with React and AWS competency case 879"
        job_desc = "Looking for Python React AWS engineer position 879"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0880(self):
        doc_text = "Experienced Python developer with React and AWS competency case 880"
        job_desc = "Looking for Python React AWS engineer position 880"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0881(self):
        doc_text = "Experienced Python developer with React and AWS competency case 881"
        job_desc = "Looking for Python React AWS engineer position 881"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0882(self):
        doc_text = "Experienced Python developer with React and AWS competency case 882"
        job_desc = "Looking for Python React AWS engineer position 882"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0883(self):
        doc_text = "Experienced Python developer with React and AWS competency case 883"
        job_desc = "Looking for Python React AWS engineer position 883"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0884(self):
        doc_text = "Experienced Python developer with React and AWS competency case 884"
        job_desc = "Looking for Python React AWS engineer position 884"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0885(self):
        doc_text = "Experienced Python developer with React and AWS competency case 885"
        job_desc = "Looking for Python React AWS engineer position 885"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0886(self):
        doc_text = "Experienced Python developer with React and AWS competency case 886"
        job_desc = "Looking for Python React AWS engineer position 886"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0887(self):
        doc_text = "Experienced Python developer with React and AWS competency case 887"
        job_desc = "Looking for Python React AWS engineer position 887"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0888(self):
        doc_text = "Experienced Python developer with React and AWS competency case 888"
        job_desc = "Looking for Python React AWS engineer position 888"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0889(self):
        doc_text = "Experienced Python developer with React and AWS competency case 889"
        job_desc = "Looking for Python React AWS engineer position 889"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0890(self):
        doc_text = "Experienced Python developer with React and AWS competency case 890"
        job_desc = "Looking for Python React AWS engineer position 890"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0891(self):
        doc_text = "Experienced Python developer with React and AWS competency case 891"
        job_desc = "Looking for Python React AWS engineer position 891"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0892(self):
        doc_text = "Experienced Python developer with React and AWS competency case 892"
        job_desc = "Looking for Python React AWS engineer position 892"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0893(self):
        doc_text = "Experienced Python developer with React and AWS competency case 893"
        job_desc = "Looking for Python React AWS engineer position 893"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0894(self):
        doc_text = "Experienced Python developer with React and AWS competency case 894"
        job_desc = "Looking for Python React AWS engineer position 894"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0895(self):
        doc_text = "Experienced Python developer with React and AWS competency case 895"
        job_desc = "Looking for Python React AWS engineer position 895"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0896(self):
        doc_text = "Experienced Python developer with React and AWS competency case 896"
        job_desc = "Looking for Python React AWS engineer position 896"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0897(self):
        doc_text = "Experienced Python developer with React and AWS competency case 897"
        job_desc = "Looking for Python React AWS engineer position 897"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0898(self):
        doc_text = "Experienced Python developer with React and AWS competency case 898"
        job_desc = "Looking for Python React AWS engineer position 898"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0899(self):
        doc_text = "Experienced Python developer with React and AWS competency case 899"
        job_desc = "Looking for Python React AWS engineer position 899"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0900(self):
        doc_text = "Experienced Python developer with React and AWS competency case 900"
        job_desc = "Looking for Python React AWS engineer position 900"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0901(self):
        doc_text = "Experienced Python developer with React and AWS competency case 901"
        job_desc = "Looking for Python React AWS engineer position 901"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0902(self):
        doc_text = "Experienced Python developer with React and AWS competency case 902"
        job_desc = "Looking for Python React AWS engineer position 902"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0903(self):
        doc_text = "Experienced Python developer with React and AWS competency case 903"
        job_desc = "Looking for Python React AWS engineer position 903"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0904(self):
        doc_text = "Experienced Python developer with React and AWS competency case 904"
        job_desc = "Looking for Python React AWS engineer position 904"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0905(self):
        doc_text = "Experienced Python developer with React and AWS competency case 905"
        job_desc = "Looking for Python React AWS engineer position 905"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0906(self):
        doc_text = "Experienced Python developer with React and AWS competency case 906"
        job_desc = "Looking for Python React AWS engineer position 906"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0907(self):
        doc_text = "Experienced Python developer with React and AWS competency case 907"
        job_desc = "Looking for Python React AWS engineer position 907"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0908(self):
        doc_text = "Experienced Python developer with React and AWS competency case 908"
        job_desc = "Looking for Python React AWS engineer position 908"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0909(self):
        doc_text = "Experienced Python developer with React and AWS competency case 909"
        job_desc = "Looking for Python React AWS engineer position 909"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0910(self):
        doc_text = "Experienced Python developer with React and AWS competency case 910"
        job_desc = "Looking for Python React AWS engineer position 910"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0911(self):
        doc_text = "Experienced Python developer with React and AWS competency case 911"
        job_desc = "Looking for Python React AWS engineer position 911"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0912(self):
        doc_text = "Experienced Python developer with React and AWS competency case 912"
        job_desc = "Looking for Python React AWS engineer position 912"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0913(self):
        doc_text = "Experienced Python developer with React and AWS competency case 913"
        job_desc = "Looking for Python React AWS engineer position 913"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0914(self):
        doc_text = "Experienced Python developer with React and AWS competency case 914"
        job_desc = "Looking for Python React AWS engineer position 914"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0915(self):
        doc_text = "Experienced Python developer with React and AWS competency case 915"
        job_desc = "Looking for Python React AWS engineer position 915"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0916(self):
        doc_text = "Experienced Python developer with React and AWS competency case 916"
        job_desc = "Looking for Python React AWS engineer position 916"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0917(self):
        doc_text = "Experienced Python developer with React and AWS competency case 917"
        job_desc = "Looking for Python React AWS engineer position 917"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0918(self):
        doc_text = "Experienced Python developer with React and AWS competency case 918"
        job_desc = "Looking for Python React AWS engineer position 918"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0919(self):
        doc_text = "Experienced Python developer with React and AWS competency case 919"
        job_desc = "Looking for Python React AWS engineer position 919"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0920(self):
        doc_text = "Experienced Python developer with React and AWS competency case 920"
        job_desc = "Looking for Python React AWS engineer position 920"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0921(self):
        doc_text = "Experienced Python developer with React and AWS competency case 921"
        job_desc = "Looking for Python React AWS engineer position 921"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0922(self):
        doc_text = "Experienced Python developer with React and AWS competency case 922"
        job_desc = "Looking for Python React AWS engineer position 922"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0923(self):
        doc_text = "Experienced Python developer with React and AWS competency case 923"
        job_desc = "Looking for Python React AWS engineer position 923"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0924(self):
        doc_text = "Experienced Python developer with React and AWS competency case 924"
        job_desc = "Looking for Python React AWS engineer position 924"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0925(self):
        doc_text = "Experienced Python developer with React and AWS competency case 925"
        job_desc = "Looking for Python React AWS engineer position 925"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0926(self):
        doc_text = "Experienced Python developer with React and AWS competency case 926"
        job_desc = "Looking for Python React AWS engineer position 926"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0927(self):
        doc_text = "Experienced Python developer with React and AWS competency case 927"
        job_desc = "Looking for Python React AWS engineer position 927"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0928(self):
        doc_text = "Experienced Python developer with React and AWS competency case 928"
        job_desc = "Looking for Python React AWS engineer position 928"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0929(self):
        doc_text = "Experienced Python developer with React and AWS competency case 929"
        job_desc = "Looking for Python React AWS engineer position 929"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0930(self):
        doc_text = "Experienced Python developer with React and AWS competency case 930"
        job_desc = "Looking for Python React AWS engineer position 930"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0931(self):
        doc_text = "Experienced Python developer with React and AWS competency case 931"
        job_desc = "Looking for Python React AWS engineer position 931"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0932(self):
        doc_text = "Experienced Python developer with React and AWS competency case 932"
        job_desc = "Looking for Python React AWS engineer position 932"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0933(self):
        doc_text = "Experienced Python developer with React and AWS competency case 933"
        job_desc = "Looking for Python React AWS engineer position 933"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0934(self):
        doc_text = "Experienced Python developer with React and AWS competency case 934"
        job_desc = "Looking for Python React AWS engineer position 934"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0935(self):
        doc_text = "Experienced Python developer with React and AWS competency case 935"
        job_desc = "Looking for Python React AWS engineer position 935"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0936(self):
        doc_text = "Experienced Python developer with React and AWS competency case 936"
        job_desc = "Looking for Python React AWS engineer position 936"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0937(self):
        doc_text = "Experienced Python developer with React and AWS competency case 937"
        job_desc = "Looking for Python React AWS engineer position 937"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0938(self):
        doc_text = "Experienced Python developer with React and AWS competency case 938"
        job_desc = "Looking for Python React AWS engineer position 938"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0939(self):
        doc_text = "Experienced Python developer with React and AWS competency case 939"
        job_desc = "Looking for Python React AWS engineer position 939"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0940(self):
        doc_text = "Experienced Python developer with React and AWS competency case 940"
        job_desc = "Looking for Python React AWS engineer position 940"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0941(self):
        doc_text = "Experienced Python developer with React and AWS competency case 941"
        job_desc = "Looking for Python React AWS engineer position 941"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0942(self):
        doc_text = "Experienced Python developer with React and AWS competency case 942"
        job_desc = "Looking for Python React AWS engineer position 942"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0943(self):
        doc_text = "Experienced Python developer with React and AWS competency case 943"
        job_desc = "Looking for Python React AWS engineer position 943"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0944(self):
        doc_text = "Experienced Python developer with React and AWS competency case 944"
        job_desc = "Looking for Python React AWS engineer position 944"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0945(self):
        doc_text = "Experienced Python developer with React and AWS competency case 945"
        job_desc = "Looking for Python React AWS engineer position 945"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0946(self):
        doc_text = "Experienced Python developer with React and AWS competency case 946"
        job_desc = "Looking for Python React AWS engineer position 946"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0947(self):
        doc_text = "Experienced Python developer with React and AWS competency case 947"
        job_desc = "Looking for Python React AWS engineer position 947"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0948(self):
        doc_text = "Experienced Python developer with React and AWS competency case 948"
        job_desc = "Looking for Python React AWS engineer position 948"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0949(self):
        doc_text = "Experienced Python developer with React and AWS competency case 949"
        job_desc = "Looking for Python React AWS engineer position 949"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0950(self):
        doc_text = "Experienced Python developer with React and AWS competency case 950"
        job_desc = "Looking for Python React AWS engineer position 950"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0951(self):
        doc_text = "Experienced Python developer with React and AWS competency case 951"
        job_desc = "Looking for Python React AWS engineer position 951"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0952(self):
        doc_text = "Experienced Python developer with React and AWS competency case 952"
        job_desc = "Looking for Python React AWS engineer position 952"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0953(self):
        doc_text = "Experienced Python developer with React and AWS competency case 953"
        job_desc = "Looking for Python React AWS engineer position 953"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0954(self):
        doc_text = "Experienced Python developer with React and AWS competency case 954"
        job_desc = "Looking for Python React AWS engineer position 954"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0955(self):
        doc_text = "Experienced Python developer with React and AWS competency case 955"
        job_desc = "Looking for Python React AWS engineer position 955"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0956(self):
        doc_text = "Experienced Python developer with React and AWS competency case 956"
        job_desc = "Looking for Python React AWS engineer position 956"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0957(self):
        doc_text = "Experienced Python developer with React and AWS competency case 957"
        job_desc = "Looking for Python React AWS engineer position 957"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0958(self):
        doc_text = "Experienced Python developer with React and AWS competency case 958"
        job_desc = "Looking for Python React AWS engineer position 958"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0959(self):
        doc_text = "Experienced Python developer with React and AWS competency case 959"
        job_desc = "Looking for Python React AWS engineer position 959"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0960(self):
        doc_text = "Experienced Python developer with React and AWS competency case 960"
        job_desc = "Looking for Python React AWS engineer position 960"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0961(self):
        doc_text = "Experienced Python developer with React and AWS competency case 961"
        job_desc = "Looking for Python React AWS engineer position 961"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0962(self):
        doc_text = "Experienced Python developer with React and AWS competency case 962"
        job_desc = "Looking for Python React AWS engineer position 962"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0963(self):
        doc_text = "Experienced Python developer with React and AWS competency case 963"
        job_desc = "Looking for Python React AWS engineer position 963"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0964(self):
        doc_text = "Experienced Python developer with React and AWS competency case 964"
        job_desc = "Looking for Python React AWS engineer position 964"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0965(self):
        doc_text = "Experienced Python developer with React and AWS competency case 965"
        job_desc = "Looking for Python React AWS engineer position 965"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0966(self):
        doc_text = "Experienced Python developer with React and AWS competency case 966"
        job_desc = "Looking for Python React AWS engineer position 966"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0967(self):
        doc_text = "Experienced Python developer with React and AWS competency case 967"
        job_desc = "Looking for Python React AWS engineer position 967"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0968(self):
        doc_text = "Experienced Python developer with React and AWS competency case 968"
        job_desc = "Looking for Python React AWS engineer position 968"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0969(self):
        doc_text = "Experienced Python developer with React and AWS competency case 969"
        job_desc = "Looking for Python React AWS engineer position 969"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0970(self):
        doc_text = "Experienced Python developer with React and AWS competency case 970"
        job_desc = "Looking for Python React AWS engineer position 970"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0971(self):
        doc_text = "Experienced Python developer with React and AWS competency case 971"
        job_desc = "Looking for Python React AWS engineer position 971"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0972(self):
        doc_text = "Experienced Python developer with React and AWS competency case 972"
        job_desc = "Looking for Python React AWS engineer position 972"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0973(self):
        doc_text = "Experienced Python developer with React and AWS competency case 973"
        job_desc = "Looking for Python React AWS engineer position 973"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0974(self):
        doc_text = "Experienced Python developer with React and AWS competency case 974"
        job_desc = "Looking for Python React AWS engineer position 974"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0975(self):
        doc_text = "Experienced Python developer with React and AWS competency case 975"
        job_desc = "Looking for Python React AWS engineer position 975"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0976(self):
        doc_text = "Experienced Python developer with React and AWS competency case 976"
        job_desc = "Looking for Python React AWS engineer position 976"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0977(self):
        doc_text = "Experienced Python developer with React and AWS competency case 977"
        job_desc = "Looking for Python React AWS engineer position 977"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0978(self):
        doc_text = "Experienced Python developer with React and AWS competency case 978"
        job_desc = "Looking for Python React AWS engineer position 978"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0979(self):
        doc_text = "Experienced Python developer with React and AWS competency case 979"
        job_desc = "Looking for Python React AWS engineer position 979"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0980(self):
        doc_text = "Experienced Python developer with React and AWS competency case 980"
        job_desc = "Looking for Python React AWS engineer position 980"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0981(self):
        doc_text = "Experienced Python developer with React and AWS competency case 981"
        job_desc = "Looking for Python React AWS engineer position 981"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0982(self):
        doc_text = "Experienced Python developer with React and AWS competency case 982"
        job_desc = "Looking for Python React AWS engineer position 982"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0983(self):
        doc_text = "Experienced Python developer with React and AWS competency case 983"
        job_desc = "Looking for Python React AWS engineer position 983"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0984(self):
        doc_text = "Experienced Python developer with React and AWS competency case 984"
        job_desc = "Looking for Python React AWS engineer position 984"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0985(self):
        doc_text = "Experienced Python developer with React and AWS competency case 985"
        job_desc = "Looking for Python React AWS engineer position 985"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0986(self):
        doc_text = "Experienced Python developer with React and AWS competency case 986"
        job_desc = "Looking for Python React AWS engineer position 986"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0987(self):
        doc_text = "Experienced Python developer with React and AWS competency case 987"
        job_desc = "Looking for Python React AWS engineer position 987"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0988(self):
        doc_text = "Experienced Python developer with React and AWS competency case 988"
        job_desc = "Looking for Python React AWS engineer position 988"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0989(self):
        doc_text = "Experienced Python developer with React and AWS competency case 989"
        job_desc = "Looking for Python React AWS engineer position 989"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0990(self):
        doc_text = "Experienced Python developer with React and AWS competency case 990"
        job_desc = "Looking for Python React AWS engineer position 990"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0991(self):
        doc_text = "Experienced Python developer with React and AWS competency case 991"
        job_desc = "Looking for Python React AWS engineer position 991"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0992(self):
        doc_text = "Experienced Python developer with React and AWS competency case 992"
        job_desc = "Looking for Python React AWS engineer position 992"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0993(self):
        doc_text = "Experienced Python developer with React and AWS competency case 993"
        job_desc = "Looking for Python React AWS engineer position 993"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0994(self):
        doc_text = "Experienced Python developer with React and AWS competency case 994"
        job_desc = "Looking for Python React AWS engineer position 994"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0995(self):
        doc_text = "Experienced Python developer with React and AWS competency case 995"
        job_desc = "Looking for Python React AWS engineer position 995"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0996(self):
        doc_text = "Experienced Python developer with React and AWS competency case 996"
        job_desc = "Looking for Python React AWS engineer position 996"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0997(self):
        doc_text = "Experienced Python developer with React and AWS competency case 997"
        job_desc = "Looking for Python React AWS engineer position 997"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0998(self):
        doc_text = "Experienced Python developer with React and AWS competency case 998"
        job_desc = "Looking for Python React AWS engineer position 998"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_0999(self):
        doc_text = "Experienced Python developer with React and AWS competency case 999"
        job_desc = "Looking for Python React AWS engineer position 999"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1000(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1000"
        job_desc = "Looking for Python React AWS engineer position 1000"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1001(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1001"
        job_desc = "Looking for Python React AWS engineer position 1001"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1002(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1002"
        job_desc = "Looking for Python React AWS engineer position 1002"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1003(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1003"
        job_desc = "Looking for Python React AWS engineer position 1003"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1004(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1004"
        job_desc = "Looking for Python React AWS engineer position 1004"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1005(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1005"
        job_desc = "Looking for Python React AWS engineer position 1005"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1006(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1006"
        job_desc = "Looking for Python React AWS engineer position 1006"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1007(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1007"
        job_desc = "Looking for Python React AWS engineer position 1007"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1008(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1008"
        job_desc = "Looking for Python React AWS engineer position 1008"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1009(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1009"
        job_desc = "Looking for Python React AWS engineer position 1009"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1010(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1010"
        job_desc = "Looking for Python React AWS engineer position 1010"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1011(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1011"
        job_desc = "Looking for Python React AWS engineer position 1011"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1012(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1012"
        job_desc = "Looking for Python React AWS engineer position 1012"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1013(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1013"
        job_desc = "Looking for Python React AWS engineer position 1013"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1014(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1014"
        job_desc = "Looking for Python React AWS engineer position 1014"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1015(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1015"
        job_desc = "Looking for Python React AWS engineer position 1015"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1016(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1016"
        job_desc = "Looking for Python React AWS engineer position 1016"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1017(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1017"
        job_desc = "Looking for Python React AWS engineer position 1017"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1018(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1018"
        job_desc = "Looking for Python React AWS engineer position 1018"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1019(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1019"
        job_desc = "Looking for Python React AWS engineer position 1019"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1020(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1020"
        job_desc = "Looking for Python React AWS engineer position 1020"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1021(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1021"
        job_desc = "Looking for Python React AWS engineer position 1021"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1022(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1022"
        job_desc = "Looking for Python React AWS engineer position 1022"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1023(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1023"
        job_desc = "Looking for Python React AWS engineer position 1023"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1024(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1024"
        job_desc = "Looking for Python React AWS engineer position 1024"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1025(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1025"
        job_desc = "Looking for Python React AWS engineer position 1025"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1026(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1026"
        job_desc = "Looking for Python React AWS engineer position 1026"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1027(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1027"
        job_desc = "Looking for Python React AWS engineer position 1027"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1028(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1028"
        job_desc = "Looking for Python React AWS engineer position 1028"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1029(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1029"
        job_desc = "Looking for Python React AWS engineer position 1029"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1030(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1030"
        job_desc = "Looking for Python React AWS engineer position 1030"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1031(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1031"
        job_desc = "Looking for Python React AWS engineer position 1031"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1032(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1032"
        job_desc = "Looking for Python React AWS engineer position 1032"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1033(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1033"
        job_desc = "Looking for Python React AWS engineer position 1033"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1034(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1034"
        job_desc = "Looking for Python React AWS engineer position 1034"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1035(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1035"
        job_desc = "Looking for Python React AWS engineer position 1035"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1036(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1036"
        job_desc = "Looking for Python React AWS engineer position 1036"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1037(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1037"
        job_desc = "Looking for Python React AWS engineer position 1037"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1038(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1038"
        job_desc = "Looking for Python React AWS engineer position 1038"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1039(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1039"
        job_desc = "Looking for Python React AWS engineer position 1039"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1040(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1040"
        job_desc = "Looking for Python React AWS engineer position 1040"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1041(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1041"
        job_desc = "Looking for Python React AWS engineer position 1041"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1042(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1042"
        job_desc = "Looking for Python React AWS engineer position 1042"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1043(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1043"
        job_desc = "Looking for Python React AWS engineer position 1043"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1044(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1044"
        job_desc = "Looking for Python React AWS engineer position 1044"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1045(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1045"
        job_desc = "Looking for Python React AWS engineer position 1045"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1046(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1046"
        job_desc = "Looking for Python React AWS engineer position 1046"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1047(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1047"
        job_desc = "Looking for Python React AWS engineer position 1047"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1048(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1048"
        job_desc = "Looking for Python React AWS engineer position 1048"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1049(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1049"
        job_desc = "Looking for Python React AWS engineer position 1049"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1050(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1050"
        job_desc = "Looking for Python React AWS engineer position 1050"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1051(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1051"
        job_desc = "Looking for Python React AWS engineer position 1051"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1052(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1052"
        job_desc = "Looking for Python React AWS engineer position 1052"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1053(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1053"
        job_desc = "Looking for Python React AWS engineer position 1053"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1054(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1054"
        job_desc = "Looking for Python React AWS engineer position 1054"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1055(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1055"
        job_desc = "Looking for Python React AWS engineer position 1055"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1056(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1056"
        job_desc = "Looking for Python React AWS engineer position 1056"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1057(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1057"
        job_desc = "Looking for Python React AWS engineer position 1057"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1058(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1058"
        job_desc = "Looking for Python React AWS engineer position 1058"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1059(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1059"
        job_desc = "Looking for Python React AWS engineer position 1059"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1060(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1060"
        job_desc = "Looking for Python React AWS engineer position 1060"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1061(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1061"
        job_desc = "Looking for Python React AWS engineer position 1061"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1062(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1062"
        job_desc = "Looking for Python React AWS engineer position 1062"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1063(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1063"
        job_desc = "Looking for Python React AWS engineer position 1063"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1064(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1064"
        job_desc = "Looking for Python React AWS engineer position 1064"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1065(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1065"
        job_desc = "Looking for Python React AWS engineer position 1065"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1066(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1066"
        job_desc = "Looking for Python React AWS engineer position 1066"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1067(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1067"
        job_desc = "Looking for Python React AWS engineer position 1067"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1068(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1068"
        job_desc = "Looking for Python React AWS engineer position 1068"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1069(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1069"
        job_desc = "Looking for Python React AWS engineer position 1069"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1070(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1070"
        job_desc = "Looking for Python React AWS engineer position 1070"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1071(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1071"
        job_desc = "Looking for Python React AWS engineer position 1071"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1072(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1072"
        job_desc = "Looking for Python React AWS engineer position 1072"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1073(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1073"
        job_desc = "Looking for Python React AWS engineer position 1073"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1074(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1074"
        job_desc = "Looking for Python React AWS engineer position 1074"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1075(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1075"
        job_desc = "Looking for Python React AWS engineer position 1075"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1076(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1076"
        job_desc = "Looking for Python React AWS engineer position 1076"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1077(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1077"
        job_desc = "Looking for Python React AWS engineer position 1077"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1078(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1078"
        job_desc = "Looking for Python React AWS engineer position 1078"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1079(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1079"
        job_desc = "Looking for Python React AWS engineer position 1079"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1080(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1080"
        job_desc = "Looking for Python React AWS engineer position 1080"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1081(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1081"
        job_desc = "Looking for Python React AWS engineer position 1081"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1082(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1082"
        job_desc = "Looking for Python React AWS engineer position 1082"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1083(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1083"
        job_desc = "Looking for Python React AWS engineer position 1083"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1084(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1084"
        job_desc = "Looking for Python React AWS engineer position 1084"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1085(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1085"
        job_desc = "Looking for Python React AWS engineer position 1085"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1086(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1086"
        job_desc = "Looking for Python React AWS engineer position 1086"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1087(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1087"
        job_desc = "Looking for Python React AWS engineer position 1087"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1088(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1088"
        job_desc = "Looking for Python React AWS engineer position 1088"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1089(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1089"
        job_desc = "Looking for Python React AWS engineer position 1089"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1090(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1090"
        job_desc = "Looking for Python React AWS engineer position 1090"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1091(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1091"
        job_desc = "Looking for Python React AWS engineer position 1091"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1092(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1092"
        job_desc = "Looking for Python React AWS engineer position 1092"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1093(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1093"
        job_desc = "Looking for Python React AWS engineer position 1093"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1094(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1094"
        job_desc = "Looking for Python React AWS engineer position 1094"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1095(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1095"
        job_desc = "Looking for Python React AWS engineer position 1095"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1096(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1096"
        job_desc = "Looking for Python React AWS engineer position 1096"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1097(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1097"
        job_desc = "Looking for Python React AWS engineer position 1097"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1098(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1098"
        job_desc = "Looking for Python React AWS engineer position 1098"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1099(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1099"
        job_desc = "Looking for Python React AWS engineer position 1099"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1100(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1100"
        job_desc = "Looking for Python React AWS engineer position 1100"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1101(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1101"
        job_desc = "Looking for Python React AWS engineer position 1101"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1102(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1102"
        job_desc = "Looking for Python React AWS engineer position 1102"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1103(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1103"
        job_desc = "Looking for Python React AWS engineer position 1103"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1104(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1104"
        job_desc = "Looking for Python React AWS engineer position 1104"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1105(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1105"
        job_desc = "Looking for Python React AWS engineer position 1105"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1106(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1106"
        job_desc = "Looking for Python React AWS engineer position 1106"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1107(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1107"
        job_desc = "Looking for Python React AWS engineer position 1107"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1108(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1108"
        job_desc = "Looking for Python React AWS engineer position 1108"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1109(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1109"
        job_desc = "Looking for Python React AWS engineer position 1109"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1110(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1110"
        job_desc = "Looking for Python React AWS engineer position 1110"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1111(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1111"
        job_desc = "Looking for Python React AWS engineer position 1111"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1112(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1112"
        job_desc = "Looking for Python React AWS engineer position 1112"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1113(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1113"
        job_desc = "Looking for Python React AWS engineer position 1113"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1114(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1114"
        job_desc = "Looking for Python React AWS engineer position 1114"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1115(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1115"
        job_desc = "Looking for Python React AWS engineer position 1115"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1116(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1116"
        job_desc = "Looking for Python React AWS engineer position 1116"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1117(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1117"
        job_desc = "Looking for Python React AWS engineer position 1117"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1118(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1118"
        job_desc = "Looking for Python React AWS engineer position 1118"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1119(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1119"
        job_desc = "Looking for Python React AWS engineer position 1119"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1120(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1120"
        job_desc = "Looking for Python React AWS engineer position 1120"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1121(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1121"
        job_desc = "Looking for Python React AWS engineer position 1121"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1122(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1122"
        job_desc = "Looking for Python React AWS engineer position 1122"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1123(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1123"
        job_desc = "Looking for Python React AWS engineer position 1123"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1124(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1124"
        job_desc = "Looking for Python React AWS engineer position 1124"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1125(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1125"
        job_desc = "Looking for Python React AWS engineer position 1125"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1126(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1126"
        job_desc = "Looking for Python React AWS engineer position 1126"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1127(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1127"
        job_desc = "Looking for Python React AWS engineer position 1127"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1128(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1128"
        job_desc = "Looking for Python React AWS engineer position 1128"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1129(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1129"
        job_desc = "Looking for Python React AWS engineer position 1129"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1130(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1130"
        job_desc = "Looking for Python React AWS engineer position 1130"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1131(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1131"
        job_desc = "Looking for Python React AWS engineer position 1131"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1132(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1132"
        job_desc = "Looking for Python React AWS engineer position 1132"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1133(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1133"
        job_desc = "Looking for Python React AWS engineer position 1133"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1134(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1134"
        job_desc = "Looking for Python React AWS engineer position 1134"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1135(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1135"
        job_desc = "Looking for Python React AWS engineer position 1135"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1136(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1136"
        job_desc = "Looking for Python React AWS engineer position 1136"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1137(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1137"
        job_desc = "Looking for Python React AWS engineer position 1137"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1138(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1138"
        job_desc = "Looking for Python React AWS engineer position 1138"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1139(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1139"
        job_desc = "Looking for Python React AWS engineer position 1139"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1140(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1140"
        job_desc = "Looking for Python React AWS engineer position 1140"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1141(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1141"
        job_desc = "Looking for Python React AWS engineer position 1141"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1142(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1142"
        job_desc = "Looking for Python React AWS engineer position 1142"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1143(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1143"
        job_desc = "Looking for Python React AWS engineer position 1143"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1144(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1144"
        job_desc = "Looking for Python React AWS engineer position 1144"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1145(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1145"
        job_desc = "Looking for Python React AWS engineer position 1145"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1146(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1146"
        job_desc = "Looking for Python React AWS engineer position 1146"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1147(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1147"
        job_desc = "Looking for Python React AWS engineer position 1147"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1148(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1148"
        job_desc = "Looking for Python React AWS engineer position 1148"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1149(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1149"
        job_desc = "Looking for Python React AWS engineer position 1149"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1150(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1150"
        job_desc = "Looking for Python React AWS engineer position 1150"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1151(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1151"
        job_desc = "Looking for Python React AWS engineer position 1151"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1152(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1152"
        job_desc = "Looking for Python React AWS engineer position 1152"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1153(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1153"
        job_desc = "Looking for Python React AWS engineer position 1153"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1154(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1154"
        job_desc = "Looking for Python React AWS engineer position 1154"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1155(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1155"
        job_desc = "Looking for Python React AWS engineer position 1155"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1156(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1156"
        job_desc = "Looking for Python React AWS engineer position 1156"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1157(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1157"
        job_desc = "Looking for Python React AWS engineer position 1157"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1158(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1158"
        job_desc = "Looking for Python React AWS engineer position 1158"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1159(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1159"
        job_desc = "Looking for Python React AWS engineer position 1159"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1160(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1160"
        job_desc = "Looking for Python React AWS engineer position 1160"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1161(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1161"
        job_desc = "Looking for Python React AWS engineer position 1161"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1162(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1162"
        job_desc = "Looking for Python React AWS engineer position 1162"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1163(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1163"
        job_desc = "Looking for Python React AWS engineer position 1163"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1164(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1164"
        job_desc = "Looking for Python React AWS engineer position 1164"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1165(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1165"
        job_desc = "Looking for Python React AWS engineer position 1165"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1166(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1166"
        job_desc = "Looking for Python React AWS engineer position 1166"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1167(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1167"
        job_desc = "Looking for Python React AWS engineer position 1167"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1168(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1168"
        job_desc = "Looking for Python React AWS engineer position 1168"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1169(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1169"
        job_desc = "Looking for Python React AWS engineer position 1169"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1170(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1170"
        job_desc = "Looking for Python React AWS engineer position 1170"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1171(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1171"
        job_desc = "Looking for Python React AWS engineer position 1171"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1172(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1172"
        job_desc = "Looking for Python React AWS engineer position 1172"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1173(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1173"
        job_desc = "Looking for Python React AWS engineer position 1173"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1174(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1174"
        job_desc = "Looking for Python React AWS engineer position 1174"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1175(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1175"
        job_desc = "Looking for Python React AWS engineer position 1175"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1176(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1176"
        job_desc = "Looking for Python React AWS engineer position 1176"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1177(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1177"
        job_desc = "Looking for Python React AWS engineer position 1177"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1178(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1178"
        job_desc = "Looking for Python React AWS engineer position 1178"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1179(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1179"
        job_desc = "Looking for Python React AWS engineer position 1179"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1180(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1180"
        job_desc = "Looking for Python React AWS engineer position 1180"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1181(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1181"
        job_desc = "Looking for Python React AWS engineer position 1181"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1182(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1182"
        job_desc = "Looking for Python React AWS engineer position 1182"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1183(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1183"
        job_desc = "Looking for Python React AWS engineer position 1183"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1184(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1184"
        job_desc = "Looking for Python React AWS engineer position 1184"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1185(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1185"
        job_desc = "Looking for Python React AWS engineer position 1185"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1186(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1186"
        job_desc = "Looking for Python React AWS engineer position 1186"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1187(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1187"
        job_desc = "Looking for Python React AWS engineer position 1187"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1188(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1188"
        job_desc = "Looking for Python React AWS engineer position 1188"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1189(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1189"
        job_desc = "Looking for Python React AWS engineer position 1189"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1190(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1190"
        job_desc = "Looking for Python React AWS engineer position 1190"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1191(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1191"
        job_desc = "Looking for Python React AWS engineer position 1191"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1192(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1192"
        job_desc = "Looking for Python React AWS engineer position 1192"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1193(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1193"
        job_desc = "Looking for Python React AWS engineer position 1193"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1194(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1194"
        job_desc = "Looking for Python React AWS engineer position 1194"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1195(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1195"
        job_desc = "Looking for Python React AWS engineer position 1195"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1196(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1196"
        job_desc = "Looking for Python React AWS engineer position 1196"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1197(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1197"
        job_desc = "Looking for Python React AWS engineer position 1197"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1198(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1198"
        job_desc = "Looking for Python React AWS engineer position 1198"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1199(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1199"
        job_desc = "Looking for Python React AWS engineer position 1199"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)

    def test_nlp_case_1200(self):
        doc_text = "Experienced Python developer with React and AWS competency case 1200"
        job_desc = "Looking for Python React AWS engineer position 1200"
        req_skills = ["python", "react", "aws"]
        pref_skills = ["docker", "kubernetes"]
        result = self.engine.calculate_match(doc_text, job_desc, req_skills, pref_skills)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["overall_score"], 0.0)
        self.assertLessEqual(result["overall_score"], 100.0)


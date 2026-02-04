from doctors_db import DOCTORS

class DoctorMatcher:
    def find_doctors(self, specialty, price_preference="medium"):
        print(f"\n[Doctor Matcher] Looking for specialty: '{specialty}'")
        print(f"[Doctor Matcher] Price preference: {price_preference}")
        
        matches = [d for d in DOCTORS if d["specialty"].lower() == specialty.lower()]
        
        print(f"[Doctor Matcher] Found {len(matches)} doctors for {specialty}")
        
        if not matches:
            print(f"[Doctor Matcher] No exact match for '{specialty}', using fallback")
            return self._find_closest_specialty(specialty)
        
        # Sort by rating first (default medium preference)
        matches.sort(key=lambda x: (-x["rating"], x["price"]))
        
        if price_preference == "low":
            matches.sort(key=lambda x: (x["price"], -x["rating"]))
        elif price_preference == "high":
            matches.sort(key=lambda x: (-x["rating"], -x["experience"]))
        
        result = matches[:3]
        print(f"[Doctor Matcher] Returning {len(result)} doctors")
        for doc in result:
            print(f"  - {doc['name']} ({doc['specialty']}) - Rating: {doc['rating']}, Price: ${doc['price']}")
        
        return result
    
    def _find_closest_specialty(self, specialty):
        all_doctors = DOCTORS.copy()
        all_doctors.sort(key=lambda x: (-x["rating"], x["price"]))
        return all_doctors[:3]

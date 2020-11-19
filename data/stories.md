## happy path
* greet
  - utter_greet

## path 1 yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* pregnant_disease{"preg":"pregnant"}
  - utter_pregnancy_check
* affirm{"result_type":"Yes"}
  - utter_menstrual_check


## path 1 no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* pregnant_disease{"preg":"pregnant"}
  - utter_pregnancy_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 2 no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 2 a yes yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexacta_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 2 a yes no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexacta_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 2 b yes yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexactb_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 2 b yes no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexactb_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 2 c yes yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexactc_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 2 c yes no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexactc_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 2 d yes yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexactd_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 2 d yes no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexactd_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 2 e yes yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexacte_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 2 e yes no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexacte_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye


## path 2 f yes yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexactf_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 2 f yes no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexactf_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye


## path 2 g yes yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexactg_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 2 g yes no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexactg_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye


## path 2 h yes yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexacth_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 2 h yes no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* sexual_active{"sex":"sexual status"}
  - utter_sexact_check
* affirm{"result_type":"Yes"}
  - utter_sexacth_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 3 a yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* urinary_question{"urine":"urinary questions"}
  - utter_urinarya_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 3 a no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* urinary_question{"urine":"urinary questions"}
  - utter_urinarya_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 3 b yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* urinary_question{"urine":"urinary questions"}
  - utter_urinaryb_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 3 b no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* urinary_question{"urine":"urinary questions"}
  - utter_urinaryb_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 3 c yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* urinary_question{"urine":"urinary questions"}
  - utter_urinaryc_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 3 c no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* urinary_question{"urine":"urinary questions"}
  - utter_urinaryc_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 3 d yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* urinary_question{"urine":"urinary questions"}
  - utter_urinaryd_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 3 d no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* urinary_question{"urine":"urinary questions"}
  - utter_urinaryd_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 3 e yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* urinary_question{"urine":"urinary questions"}
  - utter_urinarye_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye


## path 3 e no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* urinary_question{"urine":"urinary questions"}
  - utter_urinarye_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 4 hyp yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* chronic_disease{"chro":"chronic disease"}
  - utter_chronic_check
* chronic_hype{"chronic_type":"Hypertension"}
  - utter_hyper_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 4 hyp no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* chronic_disease{"chro":"chronic disease"}
  - utter_chronic_check
* chronic_hype{"chronic_type":"Hypertension"}
  - utter_hyper_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye


## path 4 diab yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* chronic_disease{"chro":"chronic disease"}
  - utter_chronic_check
* chronic_diab{"chronic_type":"Diabetes"}
  - utter_diabet_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 4 diab no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* chronic_disease{"chro":"chronic disease"}
  - utter_chronic_check
* chronic_diab{"chronic_type":"Diabetes"}
  - utter_diabet_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 5 a no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* brief_obsteric{"brief":"brief obsteric"}
  - utter_briefa_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

<!-- ## path 5 a yes
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_briefa_check
* affirm{"result_type":"Yes"}
  - utter_prega_check
* goodbye
  - utter_goodbye -->

## path 5 a yes no
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* brief_obsteric{"brief":"brief obsteric"}
  - utter_briefa_check
* affirm{"result_type":"Yes"}
  - utter_pregb_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 5 a yes yes vd
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* brief_obsteric{"brief":"brief obsteric"}
  - utter_briefa_check
* affirm{"result_type":"Yes"}
  - utter_pregb_check
* affirm{"result_type":"Yes"}
  - utter_child_check
* child_choice{"choice":"1","choice":"2","choice":"3","choice":"3+"}
  - utter_child1_check
* delivery{"delivery_type":"vaginal deliveries"}
* goodbye
  - utter_goodbye

## path 5 a yes yes cs
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* brief_obsteric{"brief":"brief obsteric"}
  - utter_briefa_check
* affirm{"result_type":"Yes"}
  - utter_pregb_check
* affirm{"result_type":"Yes"}
  - utter_child_check
* child_choice{"choice":"1","choice":"2","choice":"3","choice":"3+"}
  - utter_child1_check
* delivery{"delivery_type":"C-Section"}
* goodbye
  - utter_goodbye

## path 6 yes a
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* cervical_smears{"cerv":"cervical smears"}
  - utter_cervsma_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 6 no a
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* cervical_smears{"cerv":"cervical smears"}
  - utter_cervsma_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 6 yes b
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* cervical_smears{"cerv":"cervical smears"}
  - utter_cervsmb_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 6 no b
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* cervical_smears{"cerv":"cervical smears"}
  - utter_cervsmb_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 6 yes c
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* cervical_smears{"cerv":"cervical smears"}
  - utter_cervsmc_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 6 no c
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* cervical_smears{"cerv":"cervical smears"}
  - utter_cervsmc_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## path 6 yes d
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* cervical_smears{"cerv":"cervical smears"}
  - utter_cervsmd_check
* affirm{"result_type":"Yes"}
* goodbye
  - utter_goodbye

## path 6 no d
* greet
  - utter_greet
* symptom_checker{"symptom":"symptoms"}
  - utter_initial_bot
* decision{"decision_type":"Accept"}
  - utter_sym
* cervical_smears{"cerv":"cervical smears"}
  - utter_cervsmd_check
* deny{"result_type":"No"}
* goodbye
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye


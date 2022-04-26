from app_secrets import *

donut_value_vars=[
	'voyage_dates__imp_length_home_to_disembark',
	'voyage_dates__length_middle_passage_days',	
	'voyage_ship__tonnage_mod',
	'voyage_crew__crew_voyage_outset',
	'voyage_crew__crew_first_landing',					
	'voyage_slaves_numbers__imp_total_num_slaves_embarked',
	'voyage_slaves_numbers__imp_total_num_slaves_disembarked',
	'voyage_slaves_numbers__imp_jamaican_cash_price'
]

donut_name_vars=[
	'voyage_ship__imputed_nationality__name',
	'voyage_ship__rig_of_vessel__name',
	'voyage_outcome__particular_outcome__name',
	'voyage_outcome__outcome_slaves__name',
	'voyage_outcome__outcome_owner__name',
	'voyage_outcome__vessel_captured_outcome__name',
	'voyage_outcome__resistance__name',
	'voyage_itinerary__imp_port_voyage_begin__place',
	'voyage_itinerary__imp_region_voyage_begin__region',
	'voyage_itinerary__imp_principal_place_of_slave_purchase__place',
	'voyage_itinerary__imp_principal_region_of_slave_purchase__region',
	'voyage_itinerary__imp_principal_port_slave_dis__place',
	'voyage_itinerary__imp_principal_region_slave_dis__region',
	'voyage_itinerary__imp_broad_region_slave_dis__broad_region',
	'voyage_itinerary__place_voyage_ended__place',
	'voyage_itinerary__region_of_return__region'
	]

scatter_plot_x_vars=[
	'voyage_dates__imp_arrival_at_port_of_dis_yyyy',
	'voyage_dates__imp_length_home_to_disembark',
	'voyage_dates__length_middle_passage_days',
	'voyage_crew__crew_voyage_outset',
	'voyage_crew__crew_first_landing',
	'voyage_slaves_numbers__imp_total_num_slaves_embarked',
	'voyage_slaves_numbers__imp_total_num_slaves_disembarked'
	]

scatter_plot_y_vars=[
	'voyage_slaves_numbers__imp_total_num_slaves_embarked',
	'voyage_slaves_numbers__imp_total_num_slaves_disembarked',
	'voyage_slaves_numbers__percentage_female',
	'voyage_slaves_numbers__percentage_male',
	'voyage_slaves_numbers__percentage_child',
	'voyage_slaves_numbers__percentage_men_among_embarked_slaves',
	'voyage_slaves_numbers__percentage_women_among_embarked_slaves',
	'voyage_slaves_numbers__imp_mortality_ratio',
	'voyage_slaves_numbers__imp_jamaican_cash_price',
	'voyage_slaves_numbers__percentage_boys_among_embarked_slaves',
	'voyage_slaves_numbers__percentage_girls_among_embarked_slaves',
	'voyage_ship__tonnage_mod',
	'voyage_crew__crew_voyage_outset',
	'voyage_crew__crew_first_landing'
]

scatter_plot_factors=[
	'voyage_ship__imputed_nationality__name',
	'voyage_itinerary__imp_principal_region_of_slave_purchase__region',
	'voyage_itinerary__imp_broad_region_of_slave_purchase__broad_region',
	'voyage_itinerary__imp_broad_region_slave_dis__broad_region'
]


bar_x_vars=[
	'voyage_ship__imputed_nationality__name',
	'voyage_ship__rig_of_vessel__name',
	'voyage_outcome__particular_outcome__name',
	'voyage_outcome__outcome_slaves__name',
	'voyage_outcome__outcome_owner__name',
	'voyage_outcome__vessel_captured_outcome__name',
	'voyage_outcome__resistance__name',
	'voyage_itinerary__imp_port_voyage_begin__place',
	'voyage_itinerary__imp_region_voyage_begin__region',
	'voyage_itinerary__imp_principal_place_of_slave_purchase__place',
	'voyage_itinerary__imp_principal_region_of_slave_purchase__region',
	'voyage_itinerary__imp_principal_port_slave_dis__place',
	'voyage_itinerary__imp_principal_region_slave_dis__region',
	'voyage_itinerary__imp_broad_region_slave_dis__broad_region',
	'voyage_itinerary__place_voyage_ended__place',
	'voyage_itinerary__region_of_return__region',
	'voyage_dates__imp_arrival_at_port_of_dis_yyyy',
	'voyage_dates__voyage_began_mm',
	'voyage_dates__slave_purchase_began_mm',
	'voyage_dates__date_departed_africa_mm',
	'voyage_dates__first_dis_of_slaves_mm',
	'voyage_dates__voyage_completed_mm'
]

bar_y_abs_vars=[
	'voyage_dates__imp_length_home_to_disembark',
	'voyage_dates__length_middle_passage_days',	
	'voyage_ship__tonnage_mod',
	'voyage_crew__crew_voyage_outset',
	'voyage_crew__crew_first_landing',					
	'voyage_slaves_numbers__imp_total_num_slaves_embarked',
	'voyage_slaves_numbers__imp_total_num_slaves_disembarked',
	'voyage_slaves_numbers__imp_jamaican_cash_price'
	]

pivot_table_categorical_vars=[
	'voyage_ship__imputed_nationality__name',
	'voyage_itinerary__imp_broad_region_voyage_begin__broad_region',
	'voyage_itinerary__imp_region_voyage_begin__region',
	'voyage_itinerary__imp_port_voyage_begin__place',
	'voyage_itinerary__imp_principal_region_of_slave_purchase__region',
	'voyage_itinerary__imp_principal_place_of_slave_purchase__place',
	'voyage_itinerary__imp_principal_region_slave_dis__region',
	'voyage_itinerary__imp_broad_region_slave_dis__broad_region',
	'voyage_itinerary__imp_principal_port_slave_dis__place',
]

pivot_table_numerical_vars=[
	'voyage_dates__length_middle_passage_days',
	'voyage_slaves_numbers__imp_total_num_slaves_embarked',
	'voyage_slaves_numbers__imp_total_num_slaves_disembarked'
]

map_tilesets=[
	{"label":i[0],"value":i[1]} for i in [
	["Modern Countries","https://api.mapbox.com/styles/v1/%s/tiles/{z}/{x}/{y}?access_token=%s" %("jcm10/cl2gmkgjt000014rstx5nmcj6",mapbox_access_token)],
	["Land & Sea Only","https://api.mapbox.com/styles/v1/%s/tiles/{z}/{x}/{y}?access_token=%s" %("jcm10/cl2glcidk000k14nxnr44tu0o",mapbox_access_token)]
	]
]
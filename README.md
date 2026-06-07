# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_20:38:13_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-06-07 20:38:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-07 20:38:13 UTC

- **105,551** saved flights
- **37,146** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **105,551** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,291,522.6 tonnes** estimated CO2 emissions
- **74,870,872 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4354 |
| 2 | SkyWest Airlines | 3974 |
| 3 | IndiGo | 2098 |
| 4 | EJA | 2018 |
| 5 | American Airlines | 1693 |
| 6 | Southwest Airlines | 1595 |
| 7 | ENY | 1321 |
| 8 | Delta Air Lines | 1252 |
| 9 | Lufthansa | 1211 |
| 10 | Vueling | 971 |
| 11 | LATAM Airlines | 930 |
| 12 | WIF | 926 |
| 13 | AXM | 908 |
| 14 | AZU | 848 |
| 15 | LXJ | 794 |
| 16 | Swiss International | 765 |
| 17 | All Nippon Airways | 737 |
| 18 | Alaska Airlines | 731 |
| 19 | QLK | 708 |
| 20 | easyJet | 686 |
| 21 | EJU | 670 |
| 22 | Cathay Pacific | 629 |
| 23 | AEE | 609 |
| 24 | VIV | 604 |
| 25 | Air France | 603 |
| 26 | United Airlines | 586 |
| 27 | MXY | 575 |
| 28 | CXK | 557 |
| 29 | Japan Airlines | 525 |
| 30 | AXB | 515 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 88736 |
| 2 | 🇪🇸 ES | 7269 |
| 3 | 🇮🇳 IN | 6617 |
| 4 | 🇦🇺 AU | 6355 |
| 5 | 🇧🇷 BR | 5762 |
| 6 | 🇩🇪 DE | 5676 |
| 7 | 🇮🇹 IT | 5642 |
| 8 | 🇨🇦 CA | 5490 |
| 9 | 🇯🇵 JP | 4850 |
| 10 | 🇬🇧 GB | 4461 |
| 11 | 🇫🇷 FR | 4196 |
| 12 | 🇨🇴 CO | 3643 |
| 13 | 🇲🇽 MX | 3157 |
| 14 | 🇬🇷 GR | 3004 |
| 15 | 🇳🇴 NO | 2928 |
| 16 | 🇨🇭 CH | 2702 |
| 17 | 🇲🇾 MY | 2328 |
| 18 | 🇹🇷 TR | 2036 |
| 19 | 🇿🇦 ZA | 1818 |
| 20 | 🇳🇿 NZ | 1758 |
| 21 | 🇰🇷 KR | 1754 |
| 22 | 🇹🇭 TH | 1750 |
| 23 | 🇵🇱 PL | 1718 |
| 24 | 🇵🇭 PH | 1557 |
| 25 | 🇬🇹 GT | 1528 |
| 26 | 🇲🇦 MA | 1169 |
| 27 | 🇲🇴 MO | 1106 |
| 28 | 🇳🇱 NL | 1036 |
| 29 | 🇲🇪 ME | 1011 |
| 30 | 🇭🇷 HR | 922 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2287 |
| 2 | Denver International Airport |  | US | 1806 |
| 3 | Tokyo International Airport |  | JP | 1606 |
| 4 | Indira Gandhi International Airport |  | IN | 1439 |
| 5 | Harry Reid International Airport |  | US | 1351 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1334 |
| 7 | Guaymaral Airport |  | CO | 1327 |
| 8 | Frankfurt am Main International Airport |  | DE | 1201 |
| 9 | Zurich Airport |  | CH | 1196 |
| 10 | La Aurora Airport |  | GT | 1176 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1138 |
| 12 | El Dorado International Airport |  | CO | 1111 |
| 13 | Macau International Airport |  | MO | 1106 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1066 |
| 15 | Chicago O'Hare International Airport |  | US | 1062 |
| 16 | Madrid Barajas International Airport |  | ES | 923 |
| 17 | Kuala Lumpur International Airport |  | MY | 913 |
| 18 | Salt Lake City International Airport |  | US | 902 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 902 |
| 20 | Capua Airport |  | IT | 893 |
| 21 | Charlotte/Douglas International Airport |  | US | 819 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 810 |
| 23 | Charles de Gaulle International Airport |  | FR | 802 |
| 24 | Congonhas Airport |  | BR | 799 |
| 25 | Bengaluru International Airport |  | IN | 792 |
| 26 | Malpensa International Airport |  | IT | 790 |
| 27 | Daniel K Inouye International Airport |  | US | 720 |
| 28 | Tenerife Norte Airport |  | ES | 716 |
| 29 | Ninoy Aquino International Airport |  | PH | 713 |
| 30 | Barcelona International Airport |  | ES | 692 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 682 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 682 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 677 |
| 34 | Amsterdam Airport Schiphol |  | NL | 642 |
| 35 | Don Mueang International Airport |  | TH | 640 |
| 36 | Vitoria/Foronda Airport |  | ES | 632 |
| 37 | Calgary International Airport |  | CA | 622 |
| 38 | Seattle-Tacoma International Airport |  | US | 612 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 605 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 605 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 548 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 388 | 21m | 244 km | 1,633.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 282 | 24m | 225 km | 1,094.0 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 276 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 266 | 14m | 114 km | 521.7 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 259 | 1h 25m | 910 km | 4,064.3 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 243 | 1h 10m | 770 km | 3,228.1 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 220 | 19m | 165 km | 625.8 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 210 | 26m | 275 km | 995.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 204 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 155 | 27m | 215 km | 574.1 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 150 | 14m | 154 km | 397.4 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 146 | 31m | 369 km | 929.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 146 | 27m | 152 km | 381.6 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 142 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 139 | 18m | 144 km | 345.8 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 130 | 1h 1m | 695 km | 1,558.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 122 | 1h 43m | 1,423 km | 2,994.1 t |
| 27 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 122 | 44m | 241 km | 506.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 119 | 1h 18m | 961 km | 1,972.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N115GK |  | Francis S Gabreski Airport (KFOK) | Laguardia Airport (KLGA) | 2026-06-07 20:07 UTC | 2026-06-07 20:38 UTC | 31m |
| SPIKR12 | SPI | Victoria Regional Airport (KVCT) | Four Square Ranch Airport (3TA0) | 2026-06-07 20:10 UTC | 2026-06-07 20:37 UTC | 26m |
| N628HA |  | Truckee-Tahoe Airport (KTRK) | Truckee-Tahoe Airport (KTRK) | 2026-06-07 17:00 UTC | 2026-06-07 20:33 UTC | 3h 32m |
| VPCZS | VPC | Newark Liberty International Airport (KEWR) | Teterboro Airport (KTEB) | 2026-06-07 20:19 UTC | 2026-06-07 20:30 UTC | 10m |
| N5950K |  | Merritt Island Airport (KCOI) | Space Coast Regional Airport (KTIX) | 2026-06-07 20:12 UTC | 2026-06-07 20:24 UTC | 12m |
| LIFELN2 | LIF | City Of Colorado Springs Municipal Airport (KCOS) | Usaf Academy Davis Airfield (KAFF) | 2026-06-07 20:10 UTC | 2026-06-07 20:24 UTC | 13m |
| BRG621 | BRG | Ambler Airport (PAFM) | Robert/Bob/Curtis Memorial Airport (PFNO) | 2026-06-07 19:50 UTC | 2026-06-07 20:23 UTC | 33m |
| N80FD |  | St Louis Lambert International Airport (KSTL) | Coleman A Young Municipal Airport (KDET) | 2026-06-07 19:06 UTC | 2026-06-07 20:22 UTC | 1h 15m |
| N654WB |  | John Glenn Columbus International Airport (KCMH) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-06-07 17:35 UTC | 2026-06-07 20:19 UTC | 2h 43m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-06-07 19:37 UTC | 2026-06-07 20:17 UTC | 40m |
| N628TB |  | Ted Stevens Anchorage International Airport (PANC) | Ted Stevens Anchorage International Airport (PANC) | 2026-06-07 19:37 UTC | 2026-06-07 20:16 UTC | 39m |
| N98869 |  | Whiteman Airport (KWHP) | 8CL0 (8CL0) | 2026-06-07 17:29 UTC | 2026-06-07 20:13 UTC | 2h 44m |
| N714U |  | K2J2 (K2J2) | 9GA2 (9GA2) | 2026-06-07 20:02 UTC | 2026-06-07 20:13 UTC | 10m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-06-07 20:00 UTC | 2026-06-07 20:12 UTC | 12m |
| N108LG |  | Camarillo Airport (KCMA) | Camarillo Airport (KCMA) | 2026-06-07 20:04 UTC | 2026-06-07 20:12 UTC | 8m |
| N42SH |  | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-06-07 19:13 UTC | 2026-06-07 20:11 UTC | 57m |
| N469TS |  | Orange County Airport (KOMH) | Orange County Airport (KOMH) | 2026-06-07 19:53 UTC | 2026-06-07 20:10 UTC | 16m |
| DCM4224 | DCM | Charleston Afb/International Airport (KCHS) | Bell Strip (1NC4) | 2026-06-07 19:40 UTC | 2026-06-07 20:09 UTC | 29m |
| CFTNF | CFT | St-Jean Airport (CYJN) | Ile-aux-Grues Airport (CSH2) | 2026-06-07 18:49 UTC | 2026-06-07 20:04 UTC | 1h 15m |
| PSABS | PSA | Professor Urbano Ernesto Stumpf Airport (SBSJ) | Ubatuba Airport (SDUB) | 2026-06-07 19:50 UTC | 2026-06-07 20:03 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_13:27:32_UTC-green)

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

**Latest saved flight:** 2026-09-28 13:27:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-28 13:27:32 UTC

- **271,666** saved flights
- **79,474** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **271,666** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,293,695.1 tonnes** estimated CO2 emissions
- **190,938,846 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10686 |
| 2 | SkyWest Airlines | 9460 |
| 3 | EJA | 5319 |
| 4 | IndiGo | 4543 |
| 5 | American Airlines | 4219 |
| 6 | Southwest Airlines | 4002 |
| 7 | Delta Air Lines | 3373 |
| 8 | ENY | 3192 |
| 9 | LATAM Airlines | 2616 |
| 10 | AZU | 2550 |
| 11 | Vueling | 2259 |
| 12 | WIF | 2210 |
| 13 | LXJ | 2141 |
| 14 | Lufthansa | 2059 |
| 15 | easyJet | 1815 |
| 16 | Swiss International | 1779 |
| 17 | QLK | 1752 |
| 18 | EJU | 1698 |
| 19 | AXM | 1677 |
| 20 | United Airlines | 1661 |
| 21 | Alaska Airlines | 1604 |
| 22 | All Nippon Airways | 1560 |
| 23 | PGT | 1532 |
| 24 | GLO | 1516 |
| 25 | WMT | 1515 |
| 26 | Air France | 1495 |
| 27 | VIV | 1487 |
| 28 | Wizz Air | 1475 |
| 29 | CXK | 1336 |
| 30 | AEE | 1301 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 226336 |
| 2 | 🇪🇸 ES | 17003 |
| 3 | 🇧🇷 BR | 15918 |
| 4 | 🇦🇺 AU | 15633 |
| 5 | 🇨🇦 CA | 15144 |
| 6 | 🇮🇹 IT | 14675 |
| 7 | 🇮🇳 IN | 14378 |
| 8 | 🇩🇪 DE | 13027 |
| 9 | 🇬🇧 GB | 12564 |
| 10 | 🇨🇴 CO | 12490 |
| 11 | 🇫🇷 FR | 10793 |
| 12 | 🇯🇵 JP | 10410 |
| 13 | 🇹🇷 TR | 8223 |
| 14 | 🇬🇷 GR | 7831 |
| 15 | 🇲🇽 MX | 7494 |
| 16 | 🇨🇭 CH | 7227 |
| 17 | 🇳🇴 NO | 6712 |
| 18 | 🇹🇭 TH | 4865 |
| 19 | 🇲🇾 MY | 4541 |
| 20 | 🇿🇦 ZA | 4528 |
| 21 | 🇵🇱 PL | 4455 |
| 22 | 🇳🇿 NZ | 3820 |
| 23 | 🇵🇭 PH | 3588 |
| 24 | 🇬🇹 GT | 3422 |
| 25 | 🇭🇷 HR | 3094 |
| 26 | 🇰🇷 KR | 3068 |
| 27 | 🇲🇦 MA | 2693 |
| 28 | 🇲🇪 ME | 2547 |
| 29 | 🇳🇱 NL | 2441 |
| 30 | 🇮🇩 ID | 2262 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5533 |
| 2 | Denver International Airport |  | US | 4426 |
| 3 | Indira Gandhi International Airport |  | IN | 3249 |
| 4 | Tokyo International Airport |  | JP | 3117 |
| 5 | El Dorado International Airport |  | CO | 2970 |
| 6 | Harry Reid International Airport |  | US | 2919 |
| 7 | Guaymaral Airport |  | CO | 2827 |
| 8 | Zurich Airport |  | CH | 2816 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2721 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2607 |
| 11 | La Aurora Airport |  | GT | 2601 |
| 12 | Salt Lake City International Airport |  | US | 2401 |
| 13 | Congonhas Airport |  | BR | 2316 |
| 14 | Chicago O'Hare International Airport |  | US | 2315 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2223 |
| 16 | Capua Airport |  | IT | 2098 |
| 17 | Madrid Barajas International Airport |  | ES | 2093 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2057 |
| 19 | Frankfurt am Main International Airport |  | DE | 2053 |
| 20 | Malpensa International Airport |  | IT | 1932 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1931 |
| 22 | Charles de Gaulle International Airport |  | FR | 1931 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1910 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1904 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1825 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1762 |
| 28 | Charlotte/Douglas International Airport |  | US | 1697 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1692 |
| 30 | Barcelona International Airport |  | ES | 1684 |
| 31 | Viracopos International Airport |  | BR | 1635 |
| 32 | Kuala Lumpur International Airport |  | MY | 1627 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1596 |
| 34 | Seattle-Tacoma International Airport |  | US | 1591 |
| 35 | Calgary International Airport |  | CA | 1546 |
| 36 | Don Mueang International Airport |  | TH | 1537 |
| 37 | Bengaluru International Airport |  | IN | 1527 |
| 38 | Oslo Gardermoen Airport |  | NO | 1523 |
| 39 | Vancouver International Airport |  | CA | 1520 |
| 40 | Reno/Tahoe International Airport |  | US | 1451 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1125 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1020 | 21m | 244 km | 4,294.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 751 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 684 | 1h 6m | 770 km | 9,086.4 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 678 | 24m | 225 km | 2,630.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 454 | 44m | 555 km | 4,347.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 437 | 27m | 275 km | 2,070.8 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 430 | 1h 50m | 1,423 km | 10,552.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 416 | 44m | 241 km | 1,728.0 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 388 | 24m | 218 km | 1,461.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 379 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 367 | 21m | 250 km | 1,585.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 364 | 23m | 55 km | 346.0 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 347 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 337 | 26m | 215 km | 1,248.1 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 316 | 19m | 144 km | 786.0 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 308 | 1h 14m | 961 km | 5,105.3 t |
| 24 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 302 | 42m | 535 km | 2,789.2 t |
| 25 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 300 | 18m | 14 km | 75.0 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 294 | 1h 50m | 1,304 km | 6,614.3 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NDU322 | NDU | Mesa Gateway Airport (KIWA) | 20AZ (20AZ) | 2026-09-28 12:51 UTC | 2026-09-28 13:27 UTC | 35m |
| OEXYO | OEX | Linz Airport (LOWL) | Linz Airport (LOWL) | 2026-09-28 12:40 UTC | 2026-09-28 13:26 UTC | 45m |
| N462D |  | West Houston Airport (KIWS) | Easterwood Field (KCLL) | 2026-09-28 12:43 UTC | 2026-09-28 13:22 UTC | 39m |
| AIC8KY | Air India | Juhu Aerodrome (VAJJ) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-28 10:27 UTC | 2026-09-28 13:16 UTC | 2h 49m |
| 4XDAN |  | Bar Yehuda Airfield (LLMZ) | Bar Yehuda Airfield (LLMZ) | 2026-09-28 13:02 UTC | 2026-09-28 13:16 UTC | 13m |
| FYS52VL | FYS | Alhama De Murcia Airport (LELH) | Muchamiel Airport (LEMU) | 2026-09-28 12:32 UTC | 2026-09-28 13:16 UTC | 43m |
| HBZYW | HBZ | Wangen-Lachen Airport (LSPV) | Hausen am Albis Airport (LSZN) | 2026-09-28 12:58 UTC | 2026-09-28 13:12 UTC | 13m |
| GEIV01 | GEI | Santos Dumont Airport (SBRJ) | EMBRAER - Unidade Gaviao Peixoto Airport (SBGP) | 2026-09-28 12:16 UTC | 2026-09-28 13:09 UTC | 52m |
| N149AH |  | Kissimmee Gateway Airport (KISM) | Orlando Executive Airport (KORL) | 2026-09-28 12:56 UTC | 2026-09-28 13:05 UTC | 9m |
| DEAOB | DEA | Hildesheim Airport (EDVM) | Bonn-Hangelar Airport (EDKB) | 2026-09-28 12:04 UTC | 2026-09-28 12:58 UTC | 54m |
| N80810 |  | 02VA (02VA) | Belmont Farm Airport (88VA) | 2026-09-28 12:34 UTC | 2026-09-28 12:57 UTC | 23m |
| HBJIM | HBJ | Zurich Airport (LSZH) | Friedrichshafen Airport (EDNY) | 2026-09-28 12:26 UTC | 2026-09-28 12:56 UTC | 29m |
| TVF74JQ | TVF | Paris-Orly Airport (LFPO) | Ibiza Airport (LEIB) | 2026-09-28 11:05 UTC | 2026-09-28 12:56 UTC | 1h 50m |
| WIF8GH | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-09-28 12:27 UTC | 2026-09-28 12:53 UTC | 25m |
| THY9GQ | Turkish Airlines | Gaziemir Airport (LTBK) | Ataturk International Airport (LTBA) | 2026-09-28 12:09 UTC | 2026-09-28 12:50 UTC | 40m |
| UFX64 | UFX | Ingolstadt Manching Airport (ETSI) | Ingolstadt Manching Airport (ETSI) | 2026-09-28 12:29 UTC | 2026-09-28 12:49 UTC | 19m |
| RGA06 | RGA | Locarno Airport (LSZL) | Ambri Airport (LSPM) | 2026-09-28 12:38 UTC | 2026-09-28 12:48 UTC | 9m |
| N934CW |  | KPBI (KPBI) | Witham Field (KSUA) | 2026-09-28 12:26 UTC | 2026-09-28 12:46 UTC | 19m |
| ANE91WJ | ANE | Taza Airport (GMFZ) | Federico Garcia Lorca Airport (LEGR) | 2026-09-28 12:17 UTC | 2026-09-28 12:43 UTC | 26m |
| NIT238 | NIT | Heart Of Georgia Regional Airport (KEZM) | Heart Of Georgia Regional Airport (KEZM) | 2026-09-28 12:34 UTC | 2026-09-28 12:42 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)

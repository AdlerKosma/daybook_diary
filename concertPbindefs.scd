
/////////////////////// Pbindef's

///////////////////////
///////////////////////
///////////////////////

Pbindef(\midiMoog,
	\type, \midi,
	\midicmd, \noteOn,
	\midiout, t.midiBus,
	\chan, 0,
	\scale, Scale.minor,
	\degree, Pseq([
		Pseq([0,7,5,6,3,2,4], 1),
		Pseq([
			Pseq([2,8,0,6,7,1,4,5,3], 10),
			Pseq([1,4,5,3,6,3,2,4], 1),
			Pseq([1,0,7,5,6,3,2,4], 9)], inf)
	], 1),
	\root, Pseq([
		Pseq([-2], 30),
		Pseq([-1], 30),
		Pseq([1], 30),
		Pseq([2], inf),
	], 1),
	\dur, Pseq([
		Pseq([
			Pseq([1], 1),
			Pseq([0.1], 8),
			Pseq([0.7], 1)
		], inf),
	], inf)
);

Pbindef(\midiMoog, \dur, Pseq([Pseq([1], 4), Pseq([0.2], 10)], inf));

Pbindef(\midiMoog1,
	\type, \midi,
	\midicmd, \noteOn,
	\midiout, t.midiBus,
	\chan, 0,
	\scale, Scale.minor,
	\degree, 0,
	\root, 2,
	\dur, 1
);

Pbindef(\klank,
	\instrument, \klank,
	\scale, Scale.minor,
	\root, 2,
	\degree, Pseq([4,0,1,2,3,2,1],inf),
	\i_freq, 164.81,
	\val, 466.16,
	\dur, 1/3,
	\sus, 0.1,
	\amp1, 0.4,
	\atk, 0.01,
	\rel, 0.1,
	\outBus, t.aBus,
	\group, t.synthGroup,
);

Pbindef(\klank1,
	\instrument, \klank,
	\midinote, Pseq([
		Pseq([[64, 65, 67], [60, 62, 64]], 1),
		Pseq([[62, 65, 64], [60, 67, 69, 62]], 1),
		Pseq([[52, 69, 57,], [52, 67, 57, 53]], 1),
	], inf),
	\dur, 4,
	\i_freq, 164.81,
	\val, 466.16,
	\sus, Pkey(\dur),
	\rel, Pwhite(0.8, 1.2),
	\amp1, 0.3,
	\outBus, t.outBus,
	\group, t.synthGroup,
);

Pbindef(\panning,
	\instrument, \discreteOut,
	\group, t.panGroup,
	\inBus, t.panBusD,
	\freq, Pseq([Pseq([2,3], 4), Prand([4,5], 1)], inf),
	\dur, Pseq([
		Pseq([1], 1),
		Pseq([0.7], 1),
		Pseq([0.1], 8)
	], inf)
);

///////////////////////
///////////////////////
///////////////////////

Pbindef(\midiMoog2,
	\type, \midi,
	\group, t.synthGroup,
	\midicmd, \noteOn,
	\midiout, t.midiBus,
	\chan, 0,
	\root, -32,
	\degree, Pseq([0], inf),
	\dur, 0.5
);

///////////////////////
///////////////////////
///////////////////////
Pbindef(\grainP,
	\instrument, \bufSynth,
	\group, t.synthGroup,
	\dur, Pseq([Pseq([0.3], 15), Pseq([0.1], 10)], inf)*2,
	\buf, ~kick,
	\rel, 1,
	\rate, 1,
	\start, 0,
	\amp, 0.5,
	\outBus, t.outBus,
);

Pbindef(\midiMoog3,
	\type, \midi,
	\midicmd, \noteOn,
	\midiout, t.midiBus,
	\chan, 0,
	\root, -20,
	\degree, Pseq([Pseq([0, -2, 1], 9),Pseq([1, 2, -2], 1)], inf),
	\dur, Pseq([
		Pseq([ 0.1 ], 100),
	], inf)
);

/*Pbindef(\sawP,
\instrument, \saw,
\group, t.synthGroup,
\dur, 1/3,
\amp, 0.005,
\scale, Scale.minor,
\degree, Pseq([2,8,0,6,7,1,4,5,3],inf),
\root, -3,
\outBus, t.outBus, //OBS!!
\atk, 0.4
);*/
Pbindef(\sawP2,
	\instrument, \saw,
	\group, t.synthGroup,
	\dur, 3,
	\amp, 0.1,
	\atk, 1,
	\rel, 2,
	\scale, Scale.chromatic,
	\degree, Pseq([6,3,8], inf),
	\root, -3,
	\outBus, t.revBus
);

Pbindef(\klank1,
	\instrument, \klank,
	\scale, Scale.minor,
	\root, -1,
	\degree, Pseq([
		Pseq([3,6,2,3,2],10),
		Pseq([5,2,6,5,6],4)
	], inf),
	\i_freq, 164.81,
	\val, 466.16,
	\dur, 1/4,
	\sus, 0.1,
	\amp1, 0.4,
	\atk, 0.01,
	\rel, 0.1,
	\outBus, t.outBus,
	\group, t.synthGroup,
);

///////////////////////
///////////////////////
///////////////////////

Pbindef(\midiMoog4,
	\type, \midi,
	\midicmd, \noteOn,
	\midiout, t.midiBus,
	\chan, 0,
	\scale, Scale.minor,
	\degree, 0,
	\root, 4,
	\dur, Pseq([
		1, Pseq([1/3], 6),
		1, Pseq([1/3], 6),
		1, Pseq([1/3], 6),
		1, Pseq([1/3], 6),
		1, Pseq([2/3], 6),
		Pseq([1, Pseq([2/3], 6)], inf)
	], 1),
);

Pbindef(\midiMoog5,
	\type, \midi,
	\midicmd, \noteOn,
	\midiout, t.midiBus,
	\chan, 0,
	\scale, Scale.minor,
	\root, 4,
	\degree, 3,
	\dur, 1/3
);

Pbindef(\brownPan1,
	\instrument, \brownNoiz1,
	\group, t.synthGroup,
	\rel, 0.1,
	\dur, Pseq([
		1, Pseq([1/3], 6),
		1, Pseq([1/3], 6),
		1, Pseq([1/3], 6),
		1, Pseq([1/3], 6),
		1, Pseq([2/3], 6),
		1, Pseq([2/3], 6),
	], inf),
	\amp, Pseq([0.032, Pseq([0.015], 6)], inf)*2,
	\outBus, t.aBus
);

Pbindef(\brownPan0,
	\instrument, \brownNoiz0,
	\group, t.synthGroup,
	\freq, Pseq([
		[0,1],
		Pseq([0,1,2,3],1),
		[1,2],
		Pseq([1,2,3,0],1),
		[2,3],
		Pseq([2,3,0,1],1),
		[3,0],
		Pseq([3,0,1,2],1),
	], inf)+2,
	\rel, 0.1,
	\dur, Pseq([
		1, Pseq([1/3], 6),
		1, Pseq([1/3], 6),
		1, Pseq([1/3], 6),
		1, Pseq([1/3], 6),
		1, Pseq([2/3], 6),
	], inf),
	\amp, Pseq([0.032, Pseq([0.015], 6)], inf)*2,
);

///////////////////////
///////////////////////
///////////////////////

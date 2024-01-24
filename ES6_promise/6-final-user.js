import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = await signUpUser(firstName, lastName).then((data) => ({
    status: 'fulfilled',
    value: data,
  }));

  const filePromise = await uploadPhoto(fileName).catch((err) => ({
    status: 'rejected',
    value: err.toString(),
  }));

  return Promise.resolve([userPromise, filePromise]);
}
